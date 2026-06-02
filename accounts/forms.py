from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    company_name = forms.CharField(
        max_length=255,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control form-control-lg'
            })

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'company_name',
            'password1',
            'password2'
        )

    def save(self, commit=True):

        user = super().save(commit=True)

        CompanyProfile.objects.create(
            user=user,
            company_name=self.cleaned_data['company_name']
        )

        return user

class ProfileForm(forms.ModelForm):

    class Meta:

        model = CompanyProfile

        fields = (
            'company_name',
            'phone'
        )