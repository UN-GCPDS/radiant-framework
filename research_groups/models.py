from django.db.models import Q
from django.db import models

from typing import Iterable


# ----------------------------------------------------------------------
def to_choice(items: Iterable, prefix: str, n: int = 2) -> tuple:
    """"""
    choices = sorted(list(set(items)))
    return [(f'{prefix}{str(i).rjust(n, "0")}', choice) for i, choice in enumerate(choices, start=1)]


########################################################################
class Researcher(models.Model):
    """"""
    # ROLES = (
    # ('pr', 'Professor'),
    # ('st', 'Student'),
    # )
    first_name = models.CharField(max_length=2**6)
    last_name = models.CharField(max_length=2**6)
    # role = models.CharField(max_length=2, choices=ROLES)

    # ----------------------------------------------------------------------
    def __str__(self):
        """"""
        return self.first_name

    # ----------------------------------------------------------------------
    @property
    def full_name(self):
        """"""
        return f'{self.first_name} {self.last_name}'


########################################################################
class ResearchGroup(models.Model):
    """"""

    name = models.CharField(max_length=2**6)
    leader = models.OneToOneField(
        Researcher, on_delete=models.SET_NULL, null=True, blank=True, related_name='leader')
    # leader = models.OneToOneField(Researcher, on_delete=models.SET_NULL, null=True, blank=True, related_name='leader', limit_choices_to=Q(role='pr'))

    faculty = models.CharField(
        max_length=6, choices=to_choice(FACULTIES, prefix='fac_'))
    departament = models.CharField(
        max_length=6, choices=to_choice(DEPARTAMENTS, prefix='dep_'))

    category = models.CharField(
        max_length=6, choices=to_choice(CATEGORIES, prefix='cat_'))

    # sub_ocde = models.CharField(max_length=11, choices=to_choice(SUB_OCDE, prefix='sub_ocde_'))
    ocde = models.CharField(
        max_length=7, choices=to_choice(OCDE, prefix='ocde_'))
    knowledge = models.CharField(
        max_length=7, choices=to_choice(KNOWLEDGE, prefix='area_'))

    researchers = models.ManyToManyField(
        Researcher, related_name='researchers')

    # ----------------------------------------------------------------------
    @property
    def faculty_prety(self):
        """"""
        return dict(to_choice(self.FACULTIES, prefix='fac_')).get(self.faculty, '')

    # ----------------------------------------------------------------------
    @property
    def departament_prety(self):
        """"""
        return dict(to_choice(self.DEPARTAMENTS, prefix='dep_')).get(self.departament, '')

    # ----------------------------------------------------------------------
    @property
    def category_prety(self):
        """"""
        return dict(to_choice(self.CATEGORIES, prefix='cat_')).get(self.category, '')

