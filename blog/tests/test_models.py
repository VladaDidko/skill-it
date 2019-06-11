import pytest
from mixer.backend.django import mixer
from django.test import TestCase
from blog.models import Comment
from blog.models import Post
from blog.models import Category
from django.contrib.auth.models import User

class TestModels(TestCase):

	def test_post(self):
		title = "Test"
		post = mixer.blend('blog.post', title=title)
		self.assertEqual(post.__str__(), title)

	def test_commentTitle(self):
		comment = mixer.blend('blog.comment', text="Test")
		self.assertEqual(comment.__str__(), "Test")

	def test_commentApproval(self):
		comment = mixer.blend('blog.comment', approved_comment = False)
		comment.approve()
		assert comment.approved_comment == True

	def test_category(self):
		category = Category.objects.create(title="Test")
		self.assertEqual(category.__str__(), "Test")
		assert isinstance (category, Category)

	def test_post_instance(self):
		category = Category.objects.create(title="Test")
		user = User.objects.create();
		post = Post.objects.create(title="Test", text="Test post", author=user, category=category)
		assert isinstance(post, Post)
		