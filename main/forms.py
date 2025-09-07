from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


# ------------------------
# Registration Form
# ------------------------
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomerProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "password1": "Password",
            "password2": "Confirm Password",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": placeholders.get(field_name, "")
            })

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Ensure no duplicate across both User and CustomerProfile
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        # Step 1: Create the User
        user = super().save(commit=commit)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()

            # Step 2: Create the CustomerProfile linked to this user
            CustomerProfile.objects.create(
                user=user,
            )
        return user



# ------------------------
# Login Form
# ------------------------
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password",
        })
    )
