from django.contrib import admin
from .models import Aprendiz, Competencia, Instructor, Programa

admin.site.register(Aprendiz)
admin.site.register(Competencia)
admin.site.register(Instructor)
admin.site.register(Programa)