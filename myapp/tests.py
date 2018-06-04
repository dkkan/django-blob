# You'll need these additional imports at the top of myapp/tests.py
import datetime
from django.utils.timezone import utc
from django.test import TestCase
from django.contrib.auth.models import User

from myapp.models import Post


class PostTestCase(TestCase):
    fixtures = ['myapp/myblog_test_fixture.json',]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "A category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    fixtures = ['myapp/myblog_test_fixture.json', ]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)

        for count in range(1, 11):
            post = Post(title="Test Post %d Title" % count,
                        text="foo", author=author)

            if count < 6:
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate

            post.save()

    def test_list_only_published(self):
        resp = self.client.get('/')

        for count in range(1, 11):
            title = "Test Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)