from django.contrib.auth import forms

from .models import User

# Formulário de alteração de usuário
class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


# Formulário de criação de usuário
class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User