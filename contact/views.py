from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

from django.shortcuts import render, HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm

# Définition de la vue de contact.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            user_email = form.cleaned_data['email']
            full_message = f"Message de {user_email}:\n\n{message}"
            recipients = ['marinetognia@yahoo.fr']
            
            send_mail(subject, full_message, 'marinetognia@yahoo.fr', recipient_list=recipients)
            
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

    
def thanks(request):
    return render(request, 'contact/thanks.html')


