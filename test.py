from django.test import RequestFactory
from django.test import TestCase

from guestbook.models import Greeting
import guestbook.views


class ViewsTests(TestCase):

    """views.pyのテスト"""

    def setUp(self):
        """事前準備."""
        Greeting.objects.create(name='ゲスト1', comment='書き込み内容1\n書き込み内容1')
        Greeting.objects.create(name='ゲスト2', comment='書き込み内容2\n書き込み内容2')
        Greeting.objects.create(name='ゲスト3', comment='書き込み内容3\n書き込み内容3')
        Greeting.objects.create(name='ゲスト4', comment='書き込み内容4\n書き込み内容4')
        Greeting.objects.create(name='ゲスト5', comment='書き込み内容5\n書き込み内容5')
        Greeting.objects.create(name='ゲスト6', comment='書き込み内容6\n書き込み内容6')
        self.factory = RequestFactory()

    def test_index(self):
        """ステータス確認."""
        request = self.factory.get('/guestbook/index')
        response = guestbook.views.index(request)

        self.assertEqual(response.status_code, 200)

    def test_len(self):
        """レコード数をチェック."""
        request = self.factory.get('/guestbook/index')
        response = guestbook.views.index(request)
        greetings = response.context_data['greetings']
        self.assertEqual(len(greetings), 5)

    def test_sort(self):
        """並び順をチェック."""
        request = self.factory.get('/guestbook/index')
        response = guestbook.views.index(request)
        greetings = response.context_data['greetings']
        self.assertEqual(greetings[0].name, 'ゲスト6')
        self.assertEqual(greetings[1].name, 'ゲスト5')
        self.assertEqual(greetings[2].name, 'ゲスト4')
        self.assertEqual(greetings[3].name, 'ゲスト3')
        self.assertEqual(greetings[4].name, 'ゲスト2')
