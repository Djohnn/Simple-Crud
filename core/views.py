from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
# Create your views here.


def index(request):
    if request.method == "GET":
        usuarios= Usuario.objects.all()
        return render(request, 'index.html', {'usuarios': usuarios})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        
        usuario = Usuario(
            nome=nome,
            email=email
        )

        usuario.save()

        return redirect('/core/')
    
def deletar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('/core/')

def atualizar(request, id):
    usuarios = get_object_or_404(Usuario, id=id)
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    usuarios.nome = nome
    usuarios.email = email
    usuarios.save()

    return redirect('/core/')


