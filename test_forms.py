from django.test import RequestFactory
from django.test import TestCase

from guestbook.models import Greeting
from guestbook.forms import GreetingForm
import guestbook.views


class FormsTests(TestCase):

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

    def test_valid(self):
        """フォームの試験."""
        params = dict(name='鈴木', comment='こんにちは')
        greeting = Greeting()
        form = GreetingForm(params, instance=greeting)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        """何も入力しなければエラーになることを検証"""
        params = dict()
        greeting = Greeting()
        form = GreetingForm(params, instance=greeting)
        self.assertFalse(form.is_valid())

    def test_views_form(self):
        """views.pyで空のフォームができているか."""
        request = self.factory.get('/guestbook/index')
        response = guestbook.views.index(request)

        self.assertIsNotNone(response.context_data['form'])
