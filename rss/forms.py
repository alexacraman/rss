from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    from_email = forms.EmailField(
    widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder':'email here...'
        }
    )
    )
    
    subject = forms.CharField(
    widget=forms.TextInput(
        attrs={
            'class' : 'form-control', 
            'placeholder':'subject here...'
        }
        )
    )
    
    message = forms.CharField(
    widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder':'message here...'
        }
    
    )
    )

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email.endswith(".edu"):
            raise forms.ValidationError("This is not a valid email. Please don't use .edu.")
        return email
    
    forbidden_words = ['seo', 'ranking', 'whitehat', 'ranks','hacked','Bitcoin', 'compromised', 'organically','keywords','baclink', 'toxic', 'profile', 'toxicity','Stacking','comprehensive','metrics']

    def clean_message(self, *args, **kwargs):
        message = self.cleaned_data.get('message')
        for keyword in self.forbidden_words:
            if keyword.lower() in message.lower():
                raise forms.ValidationError("Forbidden")
        return message

    
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return False

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return False

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user