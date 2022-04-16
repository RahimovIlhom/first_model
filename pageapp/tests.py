from django.test import TestCase
# from django.urls import reverse
# from .models import Post
#
# # Create your tests here.
#
# class PostModelTest(TestCase):
#     def setUp(self):
#         Post.objects.create(title='Mavzu', text='Texting')
#
#     def test_text_content(self):
#         post = Post.objects.get(id=1)
#         excepted_object_title = f'{post.title}'
#         excepted_object_text = f'{post.text}'
#         self.assertEqual(excepted_object_title, 'Mavzu')
#         self.assertEqual(excepted_object_text, 'Texting')
#
# class HomePageViewTest(TestCase):
#     def setUp(self):
#         Post.objects.create(title='Titul', text='titul texti')
#
#     def test_views_url_exits_at_proper_location(self):
#         resp = self.client.get('/')
#         self.assertEqual(resp.status_code, 200)
#
#     def test_views_urls_by_name(self):
#         resp = self.client.get(reverse('home'))
#         self.assertEqual(resp.status_code, 200)
#
#     def test_views_urls_correct_template(self):
#         resp = self.client.get(reverse('home'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'home.html')