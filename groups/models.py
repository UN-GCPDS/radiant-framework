from django.db import models
from utils.models import Choices


########################################################################
class ResearchGroup(models.Model):
    """"""
    cod_minciencias = models.CharField('Minciencias code', primary_key=True, max_length=2**5)
    cod_hermes = models.CharField('Hermes code', max_length=2**5)

    name = models.CharField('Name', max_length=2**6)
    founded = models.DateField('Founded', default='django.utils.timezone.now')

    faculty = models.CharField('Faculty', **Choices('FACULTY'))
    departament = models.CharField('Departament', **Choices('DEPARTAMENT'))
    category = models.CharField('Category', **Choices('GROUPS_CATEGORY'))

    sub_ocde = models.CharField('SUB_OCDE', **Choices('SUB_OCDE'))
    ocde = models.CharField('OCDE', **Choices('OCDE'))
    knowledge_area = models.CharField('knowledge', **Choices('KNOWLEDGE'))

    researchers = models.ManyToManyField('researchers.Researcher', related_name='researchers')

    class Meta:
        verbose_name = "Research group"
