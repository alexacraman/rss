import urllib
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.urls import reverse_lazy
from .forms import UserCreationForm, ContactForm
from django.views import generic


from diary.models import BlogPost
from .forms import ContactForm
from .settings import DEFAULT_FROM_EMAIL


def home(request):
    latest_post = BlogPost.objects.latest('id')
    context = {
        'latest': latest_post
    }
    
    return render(request, "home.html" , context)

def about(request):
    context = {"title": "About"}
    
    return render(request, "about.html", context)


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject         = form.cleaned_data['subject']
            from_email      = form.cleaned_data['from_email']
            message         = form.cleaned_data['message']
            try:
                send_mail(subject, message+" - "+from_email, from_email, [DEFAULT_FROM_EMAIL])
               
            except BadHeaderError:
                messages.warning(request,"Invalid header discovered")
            messages.success(request, "Thank you for contacting me.")
        form = ContactForm()
    return render(request, 'email.html', {'form': form})



def gallery(request):
    return render(request, "gallery.html")


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def privacy_policy(request):
    return render(request, 'policy.html', {})

def terms_conditions(request):
    return render(request, 'terms.html', {})

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Allow: /",
    ]
    return HttpResponse("\n".join(lines), content_type='text_plain')

