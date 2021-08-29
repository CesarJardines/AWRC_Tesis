from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
#Heredo del userCreationForm que viene en django
class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
		
#Formulario  para el form de post 
class PostForm(forms.ModelForm):
	#Aqui se obtiene el campo de contenido de nuestro modelo Forms para Post
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'Ingresa tu respuesta'}))

	class Meta:
		model = Post
		fields = ['content']