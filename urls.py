from django.conf.urls import patterns, include, url
import notifications

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contatos/$', 'agenda.contatos.views.lista', name="contatos_lista"),
    url(r'^contatos/cadastro/$', 'agenda.contatos.views.cadastro', name="contatos_cadastro"),
    url(r'^contatos/salvar/$', 'agenda.contatos.views.salvar', name="contatos_salvar"),
    url(r'^contatos/editar/(?P<id>(\d+))/$', 'agenda.contatos.views.editar', name="contatos_editar"),
    url(r'^contatos/visualizar/(?P<id>(\d+))/$', 'agenda.contatos.views.visualizar', name="contatos_visualizar"),
    url(r'^contatos/atualizar/(?P<id>(\d+))/$', 'agenda.contatos.views.atualizar', name="contatos_atualizar"),
    url(r'^contatos/apagar/(?P<id>(\d+))/$', 'agenda.contatos.views.apagar', name="contatos_apagar"),
    url(r'^contatos/consulta/$', 'agenda.contatos.views.consulta', name="contatos_consulta"),
    url(r'^contatos/resultado/$', 'agenda.contatos.views.resultado', name="contatos_resultado"),
    # url('^inbox/notifications/', include(notifications.urls)),
    # edit_url = reverse('ventas:clientes_edit',kwargs={'pk':self.object.id})
)
