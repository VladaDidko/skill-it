from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.register_url = reverse('register')
		self.profile_url = reverse('profile')

	def test_register(self):
		response = self.client.get(self.register_url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'users/register.html')