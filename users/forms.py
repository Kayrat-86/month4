from django import forms
from .models import Candidate
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4}),
        }

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
