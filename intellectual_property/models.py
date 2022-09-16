from django.db import models
from utils.models import Choices


########################################################################
class Patent(models.Model):

    filed = models.CharField('Filed', primary_key=True, max_length=2**5)
    inventors = models.ManyToManyField('researchers.Professor')

    co_ownership = models.CharField('Co-ownership', max_length=2**10)
    name = models.CharField('Name', max_length=2**10)
    patent_type = models.CharField('Patent type', **Choices('PATENT_TYPE'))

    departament = models.CharField('Departament', **Choices('DEPARTAMENT'))
    grant = models.DateField('Grant', default='django.utils.timezone.now')
    filing = models.DateField('Filing', default='django.utils.timezone.now')
    publication = models.DateField('Publication', default='django.utils.timezone.now')

