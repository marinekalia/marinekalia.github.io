from django import forms

class ContactForm(forms.Form):
    CHOICES = [
        ('option1', 'Bug ou problème'),
        ('option2', 'Suggestion ou question'),
        ('option3', 'Contact urgent'),
    ]
    motif = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Motif")
    name = forms.CharField(label="Votre nom", max_length=100, required=True)
    email = forms.EmailField(label="Votre e-mail", max_length=100, required=True)
    subject = forms.CharField(label="Sujet", max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea,max_length=800, label="Votre message", required=True)
 
 

