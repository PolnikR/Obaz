from django.test import TestCase
from django.urls import reverse

from .models import DEFAULT_SERVICE_IMAGE_PATH, Services


class HomeViewTests(TestCase):
    def test_home_page_renders_default_services_when_admin_table_is_empty(self):
        response = self.client.get(reverse('home:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Priemyselné a výrobné haly')
        self.assertContains(response, 'Poľnohospodárske a skladové haly')

    def test_home_page_renders_services_from_admin_table(self):
        Services.objects.create(
            title='Servisná hala z adminu',
            short_title='Servisná hala',
            description='Popis služby spravovaný v Django admine.',
            order=1,
        )

        response = self.client.get(reverse('home:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Servisná hala z adminu')
        self.assertContains(response, 'Popis služby spravovaný v Django admine.')
        self.assertContains(response, f'/static/{DEFAULT_SERVICE_IMAGE_PATH}')
        self.assertNotContains(response, 'Poľnohospodárske a skladové haly')

    def test_home_page_prefers_uploaded_service_image(self):
        Services.objects.create(
            title='Hala s nahratým obrázkom',
            short_title='Nahratý obrázok',
            description='Popis služby s obrázkom uloženým v media.',
            image='services/custom-service.webp',
            order=1,
        )

        response = self.client.get(reverse('home:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/media/services/custom-service.webp')
        self.assertNotContains(response, f'/static/{DEFAULT_SERVICE_IMAGE_PATH}')
