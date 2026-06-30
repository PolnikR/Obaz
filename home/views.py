from django.shortcuts import render
from .models import HomePage, HomePageSectionItem


def home(request):
    page = HomePage.objects.filter(is_active=True).order_by('-updated_at').first()

    if page:
        page_content = {
            'title': page.title,
            'subtitle': page.subtitle,
            'intro': page.intro,
            'cta_text': page.cta_text,
            'cta_url': page.cta_url,
            'phone': page.phone,
            'email': page.email,
            'contact_text': page.contact_text,
            'seo_title': page.seo_title or page.title,
            'meta_description': page.meta_description or 'Oplastenie a rekonstrukcia budov a hal na kluc.',
        }
        active_items = page.items.filter(is_active=True)
        services = active_items.filter(section=HomePageSectionItem.SERVICES)
        benefits = active_items.filter(section=HomePageSectionItem.BENEFITS)
        process = active_items.filter(section=HomePageSectionItem.PROCESS)
    else:
        page_content = {
            'title': 'Montovane haly na kluc',
            'subtitle': 'Navrhujeme a realizujeme oplastenie, rekonstrukcie a montovane haly pre vyrobu, skladovanie, obchod aj sport.',
            'intro': 'Spojime technicky navrh, vyrobu konstrukcie, montaz oplastenia a dokoncovacie prace do jedneho riadeneho procesu.',
            'cta_text': 'Zaujem o halu',
            'cta_url': '#kontakt',
            'phone': '',
            'email': '',
            'contact_text': 'Napiste nam typ objektu, lokalitu a ocakavany rozsah prace. Ozveme sa s dalsim postupom a odporucanim vhodneho riesenia.',
            'seo_title': 'Montovane haly a oplastenie budov',
            'meta_description': 'Montovane haly, oplastenie budov a rekonstrukcie priemyselnych objektov na kluc.',
        }
        services = [
            {
                'title': 'Vyrobne haly',
                'description': 'Priestory pre lahku aj tazsiu vyrobu s dorazom na dispoziciu, oplastenie a technicke napojenia.',
            },
            {
                'title': 'Skladove haly',
                'description': 'Efektivne halove riesenia pre logistiku, skladovanie materialu a rychlu manipulaciu.',
            },
            {
                'title': 'Oplastenie budov',
                'description': 'Sendvicove panely, trapezove plechy a klampiarske detaily pre novostavby aj rekonstrukcie.',
            },
            {
                'title': 'Obchodne priestory',
                'description': 'Reprezentativne montovane objekty pre predajne, showroomy a prevadzkove zazemie.',
            },
            {
                'title': 'Sportove haly',
                'description': 'Velkorozponove haly s praktickym vnutornym priestorom a odolnym obvodovym plastom.',
            },
            {
                'title': 'Rekonstrukcie hal',
                'description': 'Obnova striech, fasad a oplastenia existujucich objektov bez zbytocnej novej vystavby.',
            },
        ]
        benefits = [
            {
                'title': 'Riesenie na kluc',
                'description': 'Od prveho navrhu cez dokumentaciu az po montaz riesite projekt s jednym partnerom.',
            },
            {
                'title': 'Skusenosti z realizacii',
                'description': 'Postup prace je nastaveny pre priemyselne stavby, rychle terminy a koordinaciu profesii.',
            },
            {
                'title': 'Prakticky navrh',
                'description': 'Kazde riesenie sa prisposobi prevadzke, rozpoctu, poziadavkam na izolaciu a buducemu rastu.',
            },
        ]
        process = [
            {'title': 'Konzultacia', 'description': 'Ujasnime vyuzitie haly, rozmery, lokalitu, termin a technicke poziadavky.'},
            {'title': 'Navrh a kalkulacia', 'description': 'Pripravime odporucane konstrukcne a plastove riesenie s orientacnym rozpoctom.'},
            {'title': 'Vyroba a priprava', 'description': 'Koordinujeme podklady, materialy, vyrobu konstrukcie a pripravu montaze.'},
            {'title': 'Montaz a odovzdanie', 'description': 'Zrealizujeme konstrukciu, oplastenie, detaily a odovzdame pripraveny objekt.'},
        ]

    context = {
        'page': page,
        'page_content': page_content,
        'services': services,
        'benefits': benefits,
        'process': process,
    }
    return render(request, 'home/home.html', context)
