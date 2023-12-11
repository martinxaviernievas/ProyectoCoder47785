from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse


def crear_curso(request):
    curso = Curso(nombre="Python", camada=47783)
    curso.save()
    contexto = {"curso": curso}

    return render(request, 'index.html', contexto)


def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Martin"}

    return render(request, 'index.html', contexto)
