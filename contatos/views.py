# coding: utf-8
from agenda.contatos.forms import ContatoForm
from agenda.contatos.models import Contatos
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import messages
from django.db import connection 

# Create your views here.
def lista(request):
    contatos = Contatos.objects.all()
    return render(request, 'contatos/lista.html', {'contatos':contatos})

def cadastro(request):
    return render(request, 'contatos/cadastro.html', {'form': ContatoForm()})

def editar(request, id):
    contato = Contatos.objects.get(id=id)
    form = ContatoForm(instance=contato)
        
    return render(request, 'contatos/editar.html', {'form': form, 'contato': contato})

def salvar(request):
    form = ContatoForm(request.POST)
    if ( (request.method == 'POST') and (form.is_valid()) ):
        form = form.cleaned_data
        contato = Contatos( ** form)
        contato.save(using='default')
        return HttpResponseRedirect(reverse('contatos_lista'))
    else:
        message = 'Seu formulário está em branco.'
    return HttpResponse(message)

def visualizar(request, id):
    contato = Contatos.objects.get(id=id)
    return render(request, 'contatos/visualizar.html', {'contato':contato})

def atualizar(request, id):
    form = ContatoForm(request.POST)
    if ( (request.method == 'POST') and (form.is_valid()) ):
        form = form.cleaned_data
        contato = Contatos.objects.filter(id=id).update(**form)
        # return render_to_response("contatos/lista.html", { "flash" : "Atualizado com sucesso!" } ) 
        return HttpResponseRedirect(reverse('contatos_lista'), { "flash" : "Atualizado com sucesso!" } )
        # messages.success(request, 'Atualizado com sucesso!') 
    else:
        message = 'Seu formulário está em branco.'
    return HttpResponse(message)

def apagar(request, id):
    contato = Contatos.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('contatos_lista'))

def consulta(request):
    contatos = Contatos.objects.all()
    return render(request, 'contatos/consulta.html', {'contatos':contatos})

def resultado(request):
    print 'aaaaa'