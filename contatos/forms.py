#coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from agenda.contatos.models import Contatos

# class ContatoForm(forms.Form):
#     nome = forms.CharField(required=True, label=_('Nome'))
#     endereco = forms.CharField(required=True, label=_('Endereco'))
#     sexo = forms.CharField(required=True, label=_('Sexo'))
#     email = forms.EmailField(required=True, label=_('Email'))
#     numero = forms.CharField(required=True, label=_('Numero'))
#     telefone = forms.CharField(required=True, label=_('Telefone')

class ContatoForm(forms.ModelForm):
    class Meta:
       model = Contatos