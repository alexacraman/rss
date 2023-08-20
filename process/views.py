from django.shortcuts import render
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.conf import settings

def get_csrf(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

def process_form(request):
    if request.method == 'POST':
        try:
            data = request.POST  # Parse JSON data manually
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')
            text_content = f'Web form submission from {name}, their email is {email}. There message is {message}'
            html_content =f'<!DOCTYPE html> <html> <head> <meta charset="utf-8"> <title>New Web Form Submission</title> </head> <body> <div style="font-family: Arial, sans-serif; font-size: 14px; line-height: 1.5; margin: 0; padding: 0;"> <h1 style="font-size: 18px; font-weight: normal; margin: 0 0 10px; padding: 0;">New Web Form Submission</h1> <table style="border-collapse: collapse; width: 100%;"> <tr> <td style="padding: 5px 10px; border: 1px solid #ccc;">Name:</td> <td style="padding: 5px 10px; border: 1px solid #ccc;">{ name }</td> </tr> <tr> <td style="padding: 5px 10px; border: 1px solid #ccc;">Email:</td> <td style="padding: 5px 10px; border: 1px solid #ccc;">{ email }</td> </tr> <tr> <td style="padding: 5px 10px; border: 1px solid #ccc;">Phone:</td> <td style="padding: 5px 10px; border: 1px solid #ccc;"></td> </tr> <tr> <td style="padding: 5px 10px; border: 1px solid #ccc;">Message:</td> <td style="padding: 5px 10px; border: 1px solid #ccc;">{message}</td> </tr> </table> <p style="margin-top: 20px;">Thank you for your attention to this matter.</p> <p style="margin-top: 20px;"><br> </p> </div> </body> </html>' 
            try:
                emailMessage = EmailMultiAlternatives(
                subject      = "Web Submission",
                body         = text_content,
                from_email   = settings.DEFAULT_FROM_EMAIL,
                to           = ['acramanalex@gmail.com'],
                reply_to     = [settings.DEFAULT_FROM_EMAIL]
            )
                emailMessage.attach_alternative(html_content, "text/html")
                emailMessage.send(fail_silently=False)
            except BadHeaderError as e:
                raise ValueError(e)
            return JsonResponse({'message': 'Form submitted successfully'})
        except Exception as e:
            return JsonResponse({'message': 'Error while processing form'}, status=500)

    return JsonResponse({'message': 'Invalid request'}, status=400)

