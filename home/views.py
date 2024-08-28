from django.shortcuts import render
from django.http import HttpResponse
from .forms import HospitalForm
import pandas as pd 
from joblib import load
model = load('/Users/marinetognia/Desktop/mysite/saved_models/model4.joblib')


def home(request):
    return render(request, 'home/index.html')

def categorize_age(age):
    age = int(age)  # Ensure age is an integer
    if age < 30:
        return '<30'
    elif age < 40:
        return '30-40'
    elif age < 50:
        return '40-50'
    elif age < 60:
        return '50-60'
    else:
        return '>60'

def categorize_imc(imc):
    imc = float(imc)
    if imc < 30:
        raise ValueError("IMC non valide, doit être >=30")
    elif 30 <= imc < 40:
        return '30-40'
    elif 40 <= imc < 50:
        return '40-50'
    elif imc >= 50:
        return '>50'


def score(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            # Extraction et traitement des données du formulaire
            height = request.POST.get('heightRange')
            weight = request.POST.get('weightRange')
            age = request.POST.get('ageRange')
            bmiValue = float(request.POST.get('bmiValue'))
            sexe = 'F' if request.POST.get('sexe') == 'femme' else 'H'
            reinterventions = 'Primary' if request.POST.get('reinterventions') == 'première' else 'Redo'
            type_operations = 'SLE' if request.POST.get('type_operations') == 'sleeve' else 'BPG'
            hospital_name = form.cleaned_data['hospital']

            maladie_pulmonaire = int(form.cleaned_data.get('maladie_pulmonaire', False))
            maladie_renale = int(form.cleaned_data.get('maladie_renale', False))
            maladie_foie = int(form.cleaned_data.get('maladie_foie', False))
            diabete = int(form.cleaned_data.get('diabete', False))

            # Categorisation
            age_category = categorize_age(age)
            imc_category = categorize_imc(bmiValue)
        
            # Préparation des données pour le modèle
            input_data = pd.DataFrame([{
                'sex': sexe,
                'IMC': imc_category,
                'type_chirurgie': type_operations,
                'readmissions': reinterventions,
                'age_categorie': age_category,
                'finessGeoDP': hospital_name.name,
                'renal': maladie_renale,
                'liver': maladie_foie,
                'diab': diabete,
                'pulm': maladie_pulmonaire
            }])
        
            # Prédiction
            y_pred = model.predict_proba(input_data)[:, 0][0] * 100
            
            # Catégorisation du risque
            if y_pred >= 85:
                risk_category = 'Faible'
                risk_class = 'result-low'
            elif y_pred >= 75:
                risk_category = 'Modéré'
                risk_class = 'result-moderate'
            else:
                risk_category = 'Élevé'
                risk_class = 'result-high'

            # Retourner le résultat avec la catégorie de risque
            return render(request, 'home/score.html', {
                'form': form,
                'result': f"{y_pred:.2f}",
                'risk_category': risk_category,
                'risk_class': risk_class
            })

    return render(request, 'home/score.html', {'form': form})


def about(request):
    return render(request, 'home/about_us.html')
