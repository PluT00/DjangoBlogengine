from django.test import TestCase

from blog.models import Post, Tag


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="NewPost", body="New post's body")

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/blog/post/%s/' %post.slug)

    def test_get_update_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(
            post.get_update_url(), '/blog/post/%s/edit' %post.slug
        )

    def test_get_delete_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(
            post.get_delete_url(), '/blog/post/%s/delete/' %post.slug
        )

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_slug_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEqual(max_length, 150)


class TagModelTest(TestCase):

    def setUp(self):
        Tag.objects.create(title="NewTag")

    def test_get_absolute_url(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(tag.get_absolute_url(), '/blog/tags/%s/' %tag.slug)

    def test_get_update_url(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(tag.get_update_url(), '/blog/tags/%s/edit/' %tag.slug)

    def test_get_delete_url(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(tag.get_delete_url(), '/blog/tags/%s/delete/' %tag.slug)

    def test_title_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_slug_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('slug').max_length
        self.assertEqual(max_length, 100)
