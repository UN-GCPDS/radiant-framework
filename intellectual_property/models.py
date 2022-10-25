from django.db import models
from utils.models import Choices
import json

########################################################################
class Patent(models.Model):

    filed = models.CharField('Filed', primary_key=True, max_length=2**5)
    inventors = models.ManyToManyField('researchers.Professor', related_name='patents')

    co_ownership = models.CharField('Co-ownership', max_length=2**10)
    name = models.CharField('Name', max_length=2**10)
    patent_type = models.CharField('Patent type', **Choices('PATENT_TYPE'))

    departament = models.CharField('Departament', **Choices('DEPARTAMENT'))
    grant = models.DateField('Grant', default='django.utils.timezone.now')
    filling = models.DateField('Filing', default='django.utils.timezone.now')
    publication = models.DateField('Publication', default='django.utils.timezone.now')



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
