from django.db import models


class Services(models.Model):
    title = models.CharField('nazov', max_length=140)
    short_title = models.CharField('kratky nazov', max_length=90, blank=True)
    description = models.TextField('popis')
    image_path = models.CharField(
        'cesta k obrazku v static',
        max_length=255,
        help_text='Napriklad: home/vendor/Images/oc-uvod-01.jpg',
    )
    order = models.PositiveIntegerField('poradie', default=0)
    is_active = models.BooleanField('aktivne', default=True)
    created_at = models.DateTimeField('vytvorene', auto_now_add=True)
    updated_at = models.DateTimeField('upravene', auto_now=True)

    class Meta:
        db_table = 'Services'
        ordering = ['order', 'id']
        verbose_name = 'sluzba'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
