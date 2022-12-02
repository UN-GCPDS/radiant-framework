from django.db import models
from utils.models import Choices
import json


########################################################################
class ResearchGroup(models.Model):
    """"""
    leader = models.ForeignKey('researchers.Professor', verbose_name='Lider', on_delete=models.CASCADE, null=True, blank=True, related_name='groups')
    minciencias_code = models.CharField('Código Minciencias', primary_key=True, max_length=2**5)
    hermes_code = models.CharField('Código Hermes', max_length=2**5)
    name = models.CharField('Nombre del grupo', max_length=2**7)
    research = models.CharField('Lineas de investigación', max_length=2**10)
    founded = models.DateField('Fecha de fundación', default='django.utils.timezone.now')
    faculty = models.CharField('Facultad', **Choices('FACULTY'))
    departament = models.CharField('Departamento', **Choices('DEPARTAMENT'))
    category = models.CharField('Categoria', **Choices('GROUPS_CATEGORY'))
    ocde = models.CharField('OCDE', **Choices('OCDE'))
    knowledge_area = models.CharField('Área del conocimiento', **Choices('KNOWLEDGE'))
    researchers = models.TextField('Investigadores', max_length=2**16, null=True, blank=True)
    gruplac = models.URLField('GrupLAC', null=True, blank=True)

    class Meta:
        verbose_name = "Grupo de investigación"
        verbose_name_plural = "Grupos de investigación"

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
        return f'Editar grupo de investigación (Código Minciencias: #{self.minciencias_code})'
