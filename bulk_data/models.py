from django.db import models
import pandas as pd
from researchers.models import Professor
from groups.models import ResearchGroup


########################################################################
class Bulker():

    # ----------------------------------------------------------------------
    def save(self):
        """"""
        df = pd.read_csv(self.file)

        if self.target_model.objects.count():
            actual = set([q[0] for q in self.target_model.objects.values_list('pk')])
        else:
            actual = set()

        incoming = set(df['pk'].to_list())

        to_create = incoming.difference(actual)
        to_update = actual.intersection(incoming)

        if to_create:
            bulk = [self.target_model(**self.fix_arguments(element)) for element in df.loc[df['pk'].isin(to_create)].to_dict('records')]
            self.target_model.objects.bulk_create(bulk)

        if to_update:
            bulk = [self.target_model(**self.fix_arguments(element)) for element in df.loc[df['pk'].isin(to_update)].to_dict('records')]
            fields = list(df.columns)
            fields.remove('pk')
            self.target_model.objects.bulk_update(bulk, fields=fields)

    # ----------------------------------------------------------------------
    def fix_arguments(self, element):
        """"""
        fields_in_dict = {field.name: dict([c[::-1] for c in field.choices]) for field in self.target_model._meta.fields if field.choices}
        for k in element:
            if k in fields_in_dict:
                if element[k] in fields_in_dict[k]:
                    element[k] = fields_in_dict[k][element[k]]
                else:
                    print(f'{element[k]} not in {k}')

        if 'leader' in element:
            element['leader'] = Professor.objects.get(pk=element['leader'])
        return element


########################################################################
class ProfessorBulk(Bulker, models.Model):
    """"""
    file = models.FileField('File')

    class Meta:
        verbose_name = "Update Professors database"

    @property
    def target_model(self):
        return Professor


########################################################################
class GroupsBulk(Bulker, models.Model):
    """"""
    file = models.FileField('File')

    class Meta:
        verbose_name = "Update Research groups database"

    @property
    def target_model(self):
        return ResearchGroup
