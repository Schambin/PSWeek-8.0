from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

# Create your views here.
#sempre que for criar uma nova parte, criar uma função.


def listar_cursos(request):  #resposta a requisição do cliente
    nome_filtrar = request.GET.get('nome_filtrar') #buscar por nome o curso
    carga_horaria =  request.GET.get('carga_horaria')

    cursos = Curso.objects.all()

    if nome_filtrar:
        cursos = cursos.filter(nome__contains=nome_filtrar)
    
    if carga_horaria:
        cursos = cursos.filter(carga_horaria__gte = carga_horaria)

    

    return render(request, 'listar_cursos.html', {'cursos': cursos}) #retornar na pagina o nome dos cursos

def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')
        
        return render(request, 'criar_curso.html', {'status' : status})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        carga_horaria = request.POST.get('carga_horaria')

        curso = Curso(
            nome = nome,
            carga_horaria = carga_horaria,
            data_criacao = datetime.now()
        )
        
        curso.save()
        return redirect('/curso/criar_curso/?status=1')
    
def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'ver_curso.html', {'curso':curso})

def deletar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.ativo = False
    curso.save()
    return redirect('/curso/listar_cursos/')