from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ad.models import Ad
from users.models import CustomUser


class AdTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email='test@example.ru', username='test', password='0000')
        self.ad = Ad.objects.create(title='Тестовое название объявления', description='Описание', phone_number='8-999-999-99-99', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_ad_retrieve(self):
        url = reverse('ad:ad-detail', args=(self.ad.pk,))
        data = {
            'title': 'Тестовое название объявления',
            'description': 'Описание',
            'phone_number': '8-999-999-99-99',
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.ad.title)

    def test_ad_create(self):
        url = reverse('ad:ad-list')
        data = {
            'title': 'Тестовое название объявления',
            'description': 'Описание',
            'phone_number': '8-999-999-99-99'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ad.objects.all().count(), 2)

    def test_ad_update(self):
        url = reverse('ad:ad-detail', args=(self.ad.pk,))
        data = {
            'description': 'Обновление описание'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('description'), 'Обновление описание')

    def test_ad_destroy(self):
        url = reverse('ad:ad-detail', args=(self.ad.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ad.objects.all().count(), 0)

    def test_no_forbidden(self):
        other_user = CustomUser.objects.create(email='other@example.ru', username='other', password='0000')
        self.client.force_authenticate(user=other_user)

        url = reverse('ad:ad-detail', args=(self.ad.pk,))
        data = {
            'description': 'Обновление описание',
            'owner': 'test1'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

