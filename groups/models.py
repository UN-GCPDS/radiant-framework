from django.db import models
from utils.models import Choices
import json


########################################################################
class ResearchGroup(models.Model):
    """"""
    leader = models.ForeignKey(
        'researchers.Professor', on_delete=models.CASCADE, null=True, blank=True, related_name='groups')

    minciencias_code = models.CharField(
        'Minciencias code', primary_key=True, max_length=2**5)
    hermes_code = models.CharField('Hermes code', max_length=2**5)

    name = models.CharField('Name', max_length=2**7)
    research = models.CharField('Research', max_length=2**10)
    founded = models.DateField(
        'Founded', default='django.utils.timezone.now')

    faculty = models.CharField('Faculty', **Choices('FACULTY'))
    departament = models.CharField('Departament', **Choices('DEPARTAMENT'))
    category = models.CharField('Category', **Choices('GROUPS_CATEGORY'))

    ocde = models.CharField('OCDE', **Choices('OCDE'))
    knowledge_area = models.CharField(
        'Knowledge area', **Choices('KNOWLEDGE'))

    researchers = models.TextField(
        'Researchers', max_length=2**16, null=True, blank=True)

    gruplac = models.URLField('GrupLAC', null=True, blank=True)

    class Meta:
        verbose_name = "Research group"

    # # ----------------------------------------------------------------------
    # @property
    # def category_pretty(self):
        # """"""
        # return dict(self._meta.get_field('category').choices)[getattr(self, 'category')]

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


