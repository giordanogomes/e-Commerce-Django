from django.contrib import admin
from django.contrib.auth import admin as auth_admin

# Registre seus modelos aqui.

from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
# Administrador de usuários
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm