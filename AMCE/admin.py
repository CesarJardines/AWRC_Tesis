from django.contrib import admin
from .models import Post,Profile

# Registramos nuestros modelos para poder verlos en localhost/admin

admin.site.register(Profile)
admin.site.register(Post)