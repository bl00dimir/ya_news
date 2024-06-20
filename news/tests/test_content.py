# news/tests/test_content.py
from django.conf import settings
from django.test import TestCase

from news.models import News


class TestContent(TestCase):

    @classmethod
    def setUpTestData(cls):
        for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1):
            News.objects.create(title=f'Новость {index}', text='Просто текст.')