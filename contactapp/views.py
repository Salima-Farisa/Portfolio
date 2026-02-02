from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def send_message(request):
    if request.method == "POST":
        send_mail(
            request.POST["subject"],
            request.POST["message"],
            request.POST["email"],
            [settings.DEFAULT_FROM_EMAIL],
        )
        messages.success(request, "Message sent successfully!")
    return redirect("home")
