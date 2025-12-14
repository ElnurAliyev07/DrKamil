from django.shortcuts import render
from apps.contact.models import Contact, Consultation

def contact(request):
    context = {   
        'contact_info': Contact.objects.first(),
        'consultation': Consultation.objects.first(),
    }
    return render(request, 'pages/contact/contact.html', context)

def appointment(request):
    context = {
        'contact_info': Contact.objects.first(),
        'consultation': Consultation.objects.first(),
    }
    return render(request, 'pages/contact/appointment.html', context)