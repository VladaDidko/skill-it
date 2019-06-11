from django.urls import reverse, resolve

class TestUrls:

	def test_home_url(self):
		path = reverse('home')
		assert resolve(path).view_name == 'home'

	def test_register_url(self):
		path = reverse('register')
		assert resolve(path).view_name == 'register'

	def test_login_url(self):
		path = reverse('login')
		assert resolve(path).view_name == 'login'

	def test_logout_url(self):
		path = reverse('logout')
		assert resolve(path).view_name == 'logout'

	def test_password_reset_url(self):
		path = reverse('password_reset')
		assert resolve(path).view_name == 'password_reset'

	def test_password_reset_done_url(self):
		path = reverse('password_reset_done')
		assert resolve(path).view_name == 'password_reset_done'

	def test_password_reset_confirm_url(self):
		path = reverse('password_reset_confirm', kwargs={'uidb64': 'reset122', 'token': "tsv"})
		assert resolve(path).view_name == 'password_reset_confirm'

	def test_password_reset_complete_url(self):
		path = reverse('password_reset_complete')
		assert resolve(path).view_name == 'password_reset_complete'

	def test_profile_url(self):
		path = reverse('profile')
		assert resolve(path).view_name == 'profile'

	def test_edit_profile_url(self):
		path = reverse('edit_profile')
		assert resolve(path).view_name == 'edit_profile'

	def test_my_posts_url(self):
		path = reverse('my_posts')
		assert resolve(path).view_name == 'my_posts'

	def test_people_url(self):
		path = reverse('people')
		assert resolve(path).view_name == 'people'
