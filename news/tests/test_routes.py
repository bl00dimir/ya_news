# news/tests/test_routes.py
# Импортируем класс HTTPStatus.
from http import HTTPStatus

from django.test import TestCase
# Импортируем функцию reverse().
from django.urls import reverse
from news.models import News


class TestRoutes(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(title='Заголовок', text='Текст')

    def test_home_page(self):
        # Вместо прямого указания адреса 
        # получаем его при помощи функции reverse().
        url = reverse('news:home')
        response = self.client.get(url)
        # Проверяем, что код ответа равен статусу OK (он же 200).
        self.assertEqual(response.status_code, HTTPStatus.OK)
    #Главная страница доступна анонимному пользователю. [Done!]
    #Страница отдельной новости доступна анонимному пользователю.
    #Страницы удаления и редактирования комментария доступны автору комментария.
    #При попытке перейти на страницу редактирования или удаления комментария анонимный пользователь перенаправляется на страницу авторизации.
    #Авторизованный пользователь не может зайти на страницу редактирования или удаления чужих комментариев (возвращается ошибка 404).
    #Страницы регистрации пользователей, входа в учётную запись и выхода из неё доступны анонимным пользователям.