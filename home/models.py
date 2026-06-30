from django.db import models


class HomePage(models.Model):
    title = models.CharField('nadpis', max_length=160)
    subtitle = models.CharField('podnadpis', max_length=220)
    intro = models.TextField('uvodny text')
    cta_text = models.CharField('text hlavneho tlacidla', max_length=80, default='Poziadat o cenovu ponuku')
    cta_url = models.CharField('odkaz hlavneho tlacidla', max_length=160, default='#kontakt')
    phone = models.CharField('telefon', max_length=40, blank=True)
    email = models.EmailField('email', blank=True)
    contact_text = models.TextField('kontaktna vyzva', blank=True)
    seo_title = models.CharField('SEO titulok', max_length=160, blank=True)
    meta_description = models.CharField('meta popis', max_length=220, blank=True)
    is_active = models.BooleanField('aktivna titulna stranka', default=True)
    updated_at = models.DateTimeField('upravene', auto_now=True)

    class Meta:
        verbose_name = 'titulna stranka'
        verbose_name_plural = 'titulna stranka'

    def __str__(self):
        return self.title


class HomePageSectionItem(models.Model):
    SERVICES = 'services'
    BENEFITS = 'benefits'
    PROCESS = 'process'

    SECTION_CHOICES = [
        (SERVICES, 'Sluzby'),
        (BENEFITS, 'Vyhody'),
        (PROCESS, 'Priebeh realizacie'),
    ]

    page = models.ForeignKey(
        HomePage,
        verbose_name='titulna stranka',
        related_name='items',
        on_delete=models.CASCADE,
    )
    section = models.CharField('sekcia', max_length=20, choices=SECTION_CHOICES)
    title = models.CharField('nadpis', max_length=120)
    description = models.TextField('popis')
    order = models.PositiveIntegerField('poradie', default=0)
    is_active = models.BooleanField('aktivne', default=True)

    class Meta:
        ordering = ['section', 'order', 'id']
        verbose_name = 'polozka titulnej stranky'
        verbose_name_plural = 'polozky titulnej stranky'

    def __str__(self):
        return f'{self.get_section_display()}: {self.title}'
