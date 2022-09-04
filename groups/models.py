from django.db import models
from utils.models import Choices


########################################################################
class ResearchGroup(models.Model):
    """"""
    leader = models.ForeignKey('researchers.Professor', on_delete=models.CASCADE, null=True, blank=True)

    minciencias_code = models.CharField('Minciencias code', primary_key=True, max_length=2**5)
    hermes_code = models.CharField('Hermes code', max_length=2**5)

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

    # # ----------------------------------------------------------------------
    # @property
    # def category_prety(self):
        # """"""
        # return dict(self._meta.get_field('category').choices)[getattr(self, 'category')]

    # ----------------------------------------------------------------------
    def __getattr__(self, attr):
        """"""
        if attr.endswith('_prety'):
            field = attr.replace('_prety', '')
            if field in [field.name for field in self._meta.fields]:
                return dict(self._meta.get_field(field).choices)[getattr(self, field)]

        return super().__getattr__(attr)
