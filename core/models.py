from django.db import models
from stdimage.models import StdImageField
import uuid
# Create your models here.


def get_file_path(_instance, filename):
	'''função para gerar um id unico, que será passado na hora de gerar no caminho e no da imagem'''
	ext = filename.split('.')[-1]
	filename = f'{uuid.uuid4()}.{ext}'
	return filename
	
	
	
class Base(models.Model):
	criado = models.DateField('Criação', auto_now_add=True)
	modificado = models.DateField('Atualização', auto_now=True)
	ativo = models.BooleanField('Ativo:', default=True)
	
	class Meta:
		abstract = True

class Servico(Base):
	ICONE_CHOICES = (
		('lco-cog', 'Engrenagem'),
		('lni-stats-up', 'Gráfico'),
		('lni-users', 'Usuários'),
		('lni-layers', 'Design'),
		('lni-mobile', 'Mobile'),
		('lni-rocket', 'Foguete'),
	)
	servico = models.CharField('Serviço', max_length=100)
	descricao = models.TextField(max_length=200)
	icone = models.CharField(max_length=12, choices=ICONE_CHOICES)
	
	
	
	class Meta:
		verbose_name = 'Serviço'
		verbose_name_plural = 'Serviços'
	def __str__(self):
		return self.servico
class Cargo(Base):
	cargo = models.CharField(max_length=100)
	
	class Meta:
		verbose_name = 'Cargo'
		verbose_name_plural = 'Cargos'
	def __str__(self):
		return self.cargo
class Funcionario(Base):
	nome = models.CharField(max_length=100)
	cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
	bio = models.CharField('Bio', max_length=200)
	imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
	imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {"width": 480, "height": 480, "crop": True}})
	facebook = models.CharField('Facebook', max_length=100, default='#')
	twitter = models.CharField('Twitter', max_length=100, default='#')
	instagram = models.CharField('Instagrem', max_length=100, default='#')
	
	class Meta:
		verbose_name = 'Funcionário'
		verbose_name_plural = 'Funcionários'
		
		def __str__(self):
			return self.nome

class Feature(Base):
	icone = models.CharField(max_length=12)
	titulo = models.CharField(max_length=100)
	descricao = models.CharField(max_length=200)

	class Meta:
		verbose_name = 'Feature'
		verbose_name_plural = 'Features'

	def __str__(self):
		return self.titulo
		