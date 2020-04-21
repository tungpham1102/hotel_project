from . import views
from django.test import TestCase
from django.urls import reverse, resolve


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('hotels:home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
