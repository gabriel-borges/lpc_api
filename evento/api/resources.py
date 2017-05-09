from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from evento.models import *
from django.contrib.auth.models import User

class TipoInscricaoResource(ModelResource): # OK
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "descricao": ('exact', 'startswith') # o campo descrição é para fornecer dois tipos de filtros, passando a palavra exata e um tipo de filtro
        }
        authorization = Authorization() # permite que qualquer pessoa faça requisições e chamadas na api


class PessoaResource(ModelResource): # OK
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            "nome": ('exact', 'startswith')
        }
        authorization = Authorization()


class UserResource(ModelResource): # OK
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']
        authorization = Authorization()


class EventoResource(ModelResource): # OK
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get','post','put']
        authorization = Authorization()


class EventoCientificoResource(ModelResource): # OK
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get','post','put']
        filtering = {
            "nome": ('exact', 'startswith')
        }
        authorization = Authorization()


class PessoaFisicaResource(ModelResource): # OK
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            "nome": ('exact', 'startswith')
        }
        authorization = Authorization()


class PessoaJuridicaResource(ModelResource): # OK
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()


class AutorResource(ModelResource): # OK
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()


class ArtigoCientificoResource(ModelResource): # OK
    evento = fields.ToOneField(EventoCientificoResource, 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            "titulo": ('exact', 'startswith')
        }
        authorization = Authorization()


class InscricaoResource(ModelResource): # OK
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa') # relacionamento de chave estrangeira, na tela mostra a referência da pessoa (URI)
    evento = fields.ToOneField(EventoResource, 'evento')
    tipoInscricao = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao')
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()


class ArtigoAutorResource(ModelResource): # OK
    artigoCientifico = fields.ToOneField(ArtigoCientificoResource, 'artigoCientifico')
    autor = fields.ToOneField(AutorResource, 'autor')
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()
