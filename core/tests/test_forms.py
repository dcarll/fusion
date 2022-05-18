from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):
	
	def setUp(self):
		self.nome = 'Diego Carlos'
		self.email = 'dcarlos@gmaial.com'
		self.assunto = 'Um assunto qualquer'
		self.mensagem = 'uma mensagem qualquer'
		
		self.dados = {
			'nome' : self.nome,
			'email' : self.email,
			'assunto' : self.assunto,
			'mensagem' : self.mensagem
		}
		
		self.form = ContatoForm(data=self.dados) # mesma coisa ue fazer na vies ContatoForm(request.POST)
		
		def test_enviar_email(self):
			form1 = ContatoForm(data=self.dados)
			form1.is_valid()
			res1 = form1.enviar_email()
			
			form2 = self.form
			form2.is_valid()
			res2 = form2.enviar_email()
			
			
			
			self.assertEquals(res1, res2)
