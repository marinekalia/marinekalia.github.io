function getBMIValue() {
  calculate(); // Cela mettra à jour l'IMC et la catégorie
  return document.getElementById("result").textContent;
}


document.addEventListener('DOMContentLoaded', function() {
	var form = document.querySlector('form');
	form.onsubmit = function(e) {
		e.preventDefault(); 

		// On récupère les valeurs du formulaire
		var height = document.getElementById('heightRange').value;
		var weight = document.getElementById('weightRange').value;
		var age = document.getElementById('ageRange').value;
		var bmiValue = getBMIValue();
		var sexe = document.querySelector('input[name="options"]:checked').value;
	        var reintervention = document.querySelector('input[name="reintervention"]:checked').value;
		var typeIntervention = document.querySelector('input[name="typeIntervention"]:checked').value;

		//Créer un objet avec les données 
		var data = {
			taille: height;
			poids: weight,
          		age: age,
		        imc: imc,
                        sexe: sexe,
                        reintervention: reintervention,
                        typeIntervention: typeIntervention
                };


		// Les données sont envoyées au serveur 
		fetch('url_du_serveur', {
	            method: 'POST',
	            headers: {
	                'Content-Type': 'application/json'
	            },
	            body: JSON.stringify(data)
	        })
	        .then(response => response.json())
	        .then(result => {
	            console.log(result); // Affiche le résultat (probabilité de complication)
	            // Mettre à jour l'interface utilisateur ici, par exemple :
	            // document.getElementById('predictionResult').textContent = "La probabilité de complication est de " + result.proba;
	        })
	        .catch(error => {
	            console.error('Erreur lors de la prédiction :', error);
	        });
        };

}; 
