from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
        New Contact Message

        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject=f"[Portfolio Contact] {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(request, "Message sent successfully!")
        return redirect("home")
