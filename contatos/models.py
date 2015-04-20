from django.db import models
from django.forms import ModelForm
from notifications import notify
# Create your models here.

class Contatos(models.Model):

    """Um modelo da tabela contatos."""
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    sexo =  models.CharField(choices=(
        ('m', "Masculino"),
        ('f', "Feminino"),
    ),
        max_length=1
    )
    email = models.CharField(max_length=200)
    numero = models.IntegerField(max_length=15)

    class Meta:
        ordering = ['nome']
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'
        db_table = r'contatos'
        
    def __str__(self):
        return self.nome

    # conta quantidade de contatos
    def get_nomes_count(self):
        return self.contato.count()

    # retorna a url no formato /contatos/1
    def get_contato_detail_url(self):
        return u"/contatos/%i" % self.id

    def __unicode__(self):
        return self.nome

# class ContatoForm(ModelForm):
#     class Meta:
#         model = Contatos
#         fields = ['nome','endereco','sexo','email','numero',]