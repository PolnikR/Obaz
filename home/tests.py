from django.test import TestCase
from django.urls import reverse

from .models import HomePage, HomePageSectionItem


class HomePageViewTests(TestCase):
    def test_home_page_renders_default_content(self):
        response = self.client.get(reverse('home:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Montovane haly na kluc')
        self.assertContains(response, '1000+')
        self.assertContains(response, 'Haly podla typu prevadzky')
        self.assertContains(response, 'Kontakt doplnite v administracii')

    def test_home_page_renders_admin_content(self):
        page = HomePage.objects.create(
            title='Oplastenie skladovej haly',
            subtitle='Rychla rekonstrukcia obvodoveho plasta',
            intro='Dodavka a montaz sendvicovych panelov.',
            phone='+421900111222',
            email='info@example.com',
            contact_text='Napiste nam rozmery objektu.',
        )
        HomePageSectionItem.objects.create(
            page=page,
            section=HomePageSectionItem.SERVICES,
            title='Sendvicove panely',
            description='Zateplene riesenie pre vyrobne a sklady.',
        )

        response = self.client.get(reverse('home:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Oplastenie skladovej haly')
        self.assertContains(response, 'Sendvicove panely')
        self.assertContains(response, '+421900111222')
