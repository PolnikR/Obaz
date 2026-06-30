from django.views.generic import TemplateView
from .models import Services


DEFAULT_SERVICES = [
    {
        'title': 'Priemyselné a výrobné haly',
        'short_title': 'Priemyselné a výrobné haly',
        'description': 'Veľkopriestorové stavby s dôrazom na maximálne využitie vnútorného priestranstva.',
        'image_path': 'home/vendor/Images/oc-uvod-01.jpg',
    },
    {
        'title': 'Poľnohospodárske a skladové haly',
        'short_title': 'Poľnohospodárske a skladové haly',
        'description': 'Projektované pre maximálne využitie priestoru a úsporu investičných aj prevádzkových nákladov.',
        'image_path': 'home/vendor/Images/oc-uvod-02.jpg',
    },
    {
        'title': 'Administratívne haly a predajne',
        'short_title': 'Administratívne haly a predajne',
        'description': 'Dominantné jedno či dvojposchodové stavby s modernými estetickými prvkami.',
        'image_path': 'home/vendor/Images/oc-uvod-03.jpg',
    },
    {
        'title': 'Autosalóny, autoservisy a STK',
        'short_title': 'Autosalóny, autoservisy a STK',
        'description': 'Atraktívne oceľové haly s tvorivým architektonickým stvárnením.',
        'image_path': 'home/vendor/Images/oc-uvod-04.jpg',
    },
    {
        'title': 'Športové haly a telocvične',
        'short_title': 'Športové haly a telocvične',
        'description': 'Funkčné, atraktívne a ekonomicky výhodné športové haly a telocvične.',
        'image_path': 'home/vendor/Images/oc-uvod-05.jpg',
    },
    {
        'title': 'Letecké haly a hangáry',
        'short_title': 'Letecké haly a hangáry',
        'description': 'Profesionálne riešenie pre bezpečné parkovanie a servis lietadiel či vrtuľníkov.',
        'image_path': 'home/vendor/Images/oc-uvod-07.jpg',
    },
]


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = list(Services.objects.filter(is_active=True).order_by('order', 'id'))
        context['services'] = services or DEFAULT_SERVICES
        return context
