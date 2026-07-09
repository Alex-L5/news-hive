from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post


class TestNewsViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="News title", author=self.user,
                         slug="news-title", excerpt="News excerpt",
                         content="News content", status=1)  # post_data dictionary, contains the data posted to the database
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'post_detail', args=['news-title']))  # GET request, includes the HTML content - reverse generates a URL for accessing the post_detail view  
        self.assertEqual(response.status_code, 200)  # confirms that the view responds successfully
        self.assertIn(b"News title", response.content)
        self.assertIn(b"News content", response.content)  # ensure that the content we defined for self.post is rendered
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)  # checks that the correct form is being used in the context

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }                                                   # post_data dictionary, contains the data posted to the database
        response = self.client.post(reverse(
            'post_detail', args=['news']), post_data)  # POST request, with self.client.post method
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',  # b, syntax for creating byte strings as per internet data format
            response.content
        )
