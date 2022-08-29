from django.db import models
from utils.models import Choices


########################################################################
class PersonBase(models.Model):
    """"""
    first_name = models.CharField(max_length=2**6)
    last_name = models.CharField(max_length=2**6)

    # ----------------------------------------------------------------------
    def __str__(self):
        """"""
        return self.full_name

    # ----------------------------------------------------------------------
    @property
    def full_name(self):
        """"""
        return f'{self.first_name} {self.last_name}'

    # ----------------------------------------------------------------------
    def fix_name(name: str) -> dict:
        """"""
        name = name.lower().replace(' del', '_del').replace(' de', '_de').strip().split()
        match len(name):

            case 1:  # only first name
                return {'first_name': ''.join(name).title()}

            case 2:  # one first name and one last name
                return {'first_name': name[1].title(),
                        'last_name': name[0].title()}

            case 3:  # one first name and two last name
                return {'first_name': name[-1],
                        'last_name': ' '.join(name[:-1]).replace('_', ' ').title()}

            case 4:  # first name and last name
                return {'first_name': ' '.join(name[-2:]).replace('_', ' ').title(),
                        'last_name': ' '.join(name[:-2]).replace('_', ' ').title()}


########################################################################
class Professor(PersonBase):
    """"""
    ID = models.BigIntegerField('ID', primary_key=True)
    category = models.CharField('category', **Choices('RESEARCHER_CATEGORY'))

    faculty = models.CharField('faculty', **Choices('FACULTY'))
    departament = models.CharField('departament', **Choices('DEPARTAMENT'))

    class Meta:
        verbose_name = "Professor"


########################################################################
class Researcher(PersonBase):
    """"""
    # ID = models.BigIntegerField('ID', primary_key=True)
    joined = models.DateField('Join', default='django.utils.timezone.now')
    departed = models.DateField('Departed', null=True, blank=True)

    class Meta:
        verbose_name = "Researcher"
