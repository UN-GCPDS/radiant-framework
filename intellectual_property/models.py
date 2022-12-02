from django.db import models
from utils.models import Choices
import json

########################################################################
class Patent(models.Model):

    filed = models.CharField('Radicado', primary_key=True, max_length=2**5)
    inventors = models.ManyToManyField('researchers.Professor', related_name='patents')

    co_ownership = models.CharField('Cotitularidad', help_text='Separados por coma (,)', max_length=2**10)
    name = models.CharField('Nombre de la patente', max_length=2**10)
    patent_type = models.CharField('Tipo de patente', **Choices('PATENT_TYPE'))

    departament = models.CharField('Departamento', **Choices('DEPARTAMENT'))
    grant = models.DateField('Fecha de concesión', default='django.utils.timezone.now')
    filling = models.DateField('Fecha de presentación', default='django.utils.timezone.now')
    publication = models.DateField('Fecha de publicación', default='django.utils.timezone.now')


    # ----------------------------------------------------------------------
    class Meta:
        verbose_name = "Patente"

    # ----------------------------------------------------------------------
    def __getattr__(self, attr):
        """"""
        if attr.endswith('_pretty'):
            field = attr.replace('_pretty', '')
            if field in [field.name for field in self._meta.fields]:
                return dict(self._meta.get_field(field).choices).get(getattr(self, field), '')

        elif attr.endswith('_json'):
            field = attr.replace('_json', '')
            return json.loads(getattr(self, field))

        return super().__getattr__(attr)

    # ----------------------------------------------------------------------
    def __str__(self):
        return f'Patente (ID:#{self.pk})'
