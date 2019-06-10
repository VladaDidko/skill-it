from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.list_url = reverse('post_list')
		self.category_list = reverse('category_list', args = ['Sport'])

	def test_post_list(self):
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_list.html')

	def test_category_list(self):
		response = self.client.get(self.category_list)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_list.html')
		