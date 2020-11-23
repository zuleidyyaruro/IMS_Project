from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render

# Create your views here.
from django.template import RequestContext

def contactomail(request):
    if request.method == 'POST':
        subject = request.POST['asunto']
        message = request.POST['mensaje'] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["zvyaruro@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'gracias.html')

    return render(request, "contacto.html")
