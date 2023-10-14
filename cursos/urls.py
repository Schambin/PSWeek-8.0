from django.urls import path
from . import views

#aqui direciona a url para aonde você quer de acordo com a views.py
urlpatterns = [   
    path('listar_cursos/',views.listar_cursos, name="listar_cursos"),
    path('criar_curso/',views.criar_curso, name="criar_curso"),
    path('ver_curso/<int:id>', views.ver_curso, name="ver_curso"), #url dinamica
    path('deletar_curso/<int:id>', views.deletar_curso, name="deletar_curso")
]