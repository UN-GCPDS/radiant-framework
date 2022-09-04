from django.db import models
from utils.models import Choices


########################################################################
class Call:
    """"""
    name = models.CharField('Name', max_length=2**7)
    date = models.DateField('Date', auto_now_add=True)
    call_type = models.CharField('Type', **Choices('CALL_TYPE'))


########################################################################
class Project:
    """"""
    call = models.ForeignKey('projefcts.Call', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=2**8)
    director = models.ForeignKey('researchers.Professor', on_delete=models.CASCADE)
    state = models.CharField('Type', **Choices('PROJECT_STATE'))

    start_date = models.DateField('Start', auto_now=True)
    end_date = models.DateField('End', auto_now=True)

    aval = models.BigIntegerField('Aval')
    hermes_code = models.CharField('Hermes code', max_length=2**4)
    quipu_code = models.CharField('Quipu code', max_length=2**4)
