from django.urls import reverse, resolve

class TestUrls:

	def test_detail_url(self):
		path = reverse('post_details', kwargs={'pk': 1})
		assert resolve(path).view_name == 'post_details'

	def test_post_list_url(self):
		path = reverse('post_list')
		assert resolve(path).view_name == 'post_list'

	def test_category_list_url(self):
		path = reverse('category_list', kwargs={'slug': 'Sport'})
		assert resolve(path).view_name == 'category_list'

	def test_add_comment_to_post_url(self):
		path = reverse('add_comment_to_post', kwargs={'pk': '1'})
		assert resolve(path).view_name == 'add_comment_to_post'

	def test_comment_approve_url(self):
		path = reverse('comment_approve', kwargs={'pk': '1'})
		assert resolve(path).view_name == 'comment_approve'

	def test_comment_remove_url(self):
		path = reverse('comment_remove', kwargs={'pk': '1'})
		assert resolve(path).view_name == 'comment_remove'
		