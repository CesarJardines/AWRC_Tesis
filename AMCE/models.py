from django.db import models
#se importan el modelo Usuario que viene por defecto en Django
from django.contrib.auth.models import User
#se importa la zona horaria 
from django.utils import timezone 

#modelo equipo para mostrar todos los post de los integrantes de equipo
class Equipo(models.Model):
	nombre = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

#Creación del modelo para los perfiles de los usuarios
class Profile(models.Model):
	'''
	Atributos de Profile
	on_delete es por si ADMIN elimina un usuario también se elimina con el perfil
	'''
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=False, blank=False, default=None)
	#image = models.ImageField(default="profile.png")

	def __str__(self):
		return f'Perfil de {self.user.username}'

#Creación del modelo para los post de los alumnos en los pasos de MG
class Post(models.Model):
	'''
	Atributos de Post
	'''
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
	timestamp = models.DateTimeField(default = timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']
	#str necesario para visualizar el contenido del post en local/admin/post
	def __str__(self):
		return f'{self.user.username}: {self.content}'
