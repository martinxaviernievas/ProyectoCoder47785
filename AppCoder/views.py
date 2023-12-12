from django.shortcuts import render, redirect
from AppCoder.models import Curso, Estudiante

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos
    }
    return render(request, "AppCoder/cursos.html", contexto)

def crear_curso(request):
    nuevo_curso = Curso(nombre="Python", camada=4778383)
    nuevo_curso.save()
    return redirect("/app/cursos")

def show_html(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos, "nombre": "Martin"}
    return render(request, 'index.html', contexto)

