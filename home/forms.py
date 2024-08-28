from django import forms
from home.models import HospitalName

class HospitalForm(forms.Form):
    hospital = forms.ModelChoiceField(queryset=HospitalName.objects.all(), empty_label="Sélectionnez un hôpital")


class PatientForm(forms.Form):
    heightRange = forms.IntegerField(label='Taille', min_value=100, max_value=220, required=True)
    weightRange = forms.IntegerField(label='Poids', min_value=40, max_value=300, required=True)
    ageRange = forms.IntegerField(label='Âge', min_value=18, max_value=80, required=True)
    bmiValue = forms.FloatField(label="IMC", widget=forms.HiddenInput(),required=True)


    choix_sex = [
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ]
    sexe = forms.ChoiceField(label='Sexe', choices=choix_sex, widget=forms.RadioSelect)

    choix_reinterventions = [
        ('première', 'Première'),
        ('seconde', 'Seconde'),
    ]
    reinterventions = forms.ChoiceField(label='Réinterventions', choices=choix_reinterventions, widget=forms.RadioSelect)

    choix_operations = [
        ('sleeve', 'Sleeve Gastrectomie'),
        ('bypass', 'Bypass Gastrique'),
    ]
    type_operations = forms.ChoiceField(label="Type d'Intervention", choices=choix_operations, widget=forms.RadioSelect)

    maladie_pulmonaire = forms.BooleanField(label="Maladie pulmonaire", required=False)
    maladie_renale = forms.BooleanField(label="Maladie rénale", required=False)
    maladie_foie = forms.BooleanField(label="Maladie du foie", required=False)
    diabete = forms.BooleanField(label="Diabète", required=False)
