from django.shortcuts import render
from .models import Aprendiz


def lista_aprendices(request):
    aprendices = Aprendiz.objects.select_related('programa').all()
    return render(request, 'index.html', {'aprendices': aprendices})