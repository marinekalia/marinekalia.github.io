function calculate() {
  var bmi;
  var result = document.getElementById("result");

  var weightRange = parseInt(document.getElementById("weightRange").value);
  document.getElementById("weightValue").textContent = weightRange + " kg";

  var heightRange = parseInt(document.getElementById("heightRange").value);
  document.getElementById("heightValue").textContent = heightRange + " cm";

  bmi = (weightRange / Math.pow((heightRange / 100), 2)).toFixed(1);
  result.textContent = bmi;
  document.getElementById("bmiValue").value = bmi;
  

  var category; 
  if (bmi < 18.5) {
    category = "Sous-poids";
    result.style.color = "#feb236";
  } else if (bmi >= 18.5 && bmi <= 24.9) {
    category = "Poids Normal";
    result.style.color = "#b5e7a0";
  } else if (bmi >= 25 && bmi <= 29.9) {
    category = "Surpoids";
    result.style.color = "#fe715e";
  } else if (bmi >= 30 && bmi <= 34.9) {
    category = "Obésité classe I";
    result.style.color = "#dc3e32";
  } else if (bmi >= 35 && bmi <= 39.9)  {
    category = "Obésité classe II";
    result.style.color = "#b63726";
  } else {
    category = "Obésité classe III";
    result.style.color = "#8c2b1e";
  } 
  document.getElementById("category").textContent = category;
}


