from django.test import TestCase
from django.urls import reverse
from .models import Posts


class PostsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Posts.objects.create(title='Post 1',
                             content='Description 1', author='User 1')

    def test_post_has_title(self):
        post = Posts.objects.get(id=1)
        self.assertEqual(post.title, 'Post 1')

    def test_post_has_content(self):
        post = Posts.objects.get(id=1)
        self.assertEqual(post.content, 'Description 1')

    def test_post_has_author(self):
        post = Posts.objects.get(id=1)
        self.assertEqual(post.author, 'User 1')


class PostsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in [1, 2, 3, 4, 5]:
            Posts.objects.create(title=f'Post {i}', content=f'Description {i}',
                                 author=f'User {i}')

    def test_post_get_all_returns_all_posts(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

        for i in [1, 2, 3, 4, 5]:
            self.assertContains(response, f'Post {i}')
            self.assertContains(response, f'Description {i}')
            self.assertContains(response, f'User {i}')

    def test_post_get_returns_post(self):
        post = Posts.objects.get(id=1)
        response = self.client.get(reverse('post', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post 1')

    def test_delete_should_remove_item(self):
        posts = Posts.objects.all()
        initial_length = posts.count()
        post = Posts.objects.get(id=1)
        response = self.client.get(reverse('delete_post', args=[post.id]))
        final_length = Posts.objects.all().count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(initial_length, final_length+1)
