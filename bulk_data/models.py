from django.db import models
import pandas as pd
from researchers.models import Professor
from groups.models import ResearchGroup
from intellectual_property.models import Patent
import json

bulk_models = {
    'bulk_Professor': Professor,
    'bulk_ResearchGroup': ResearchGroup,
    'bulk_Patent': Patent,
}


########################################################################
class Bulker():

    # ----------------------------------------------------------------------
    def save(self):
        """"""
        for field in [f.name for f in self._meta.fields if f.name.startswith('bulk')]:
            if not bool(getattr(self, field)):
                continue
            df = pd.read_csv(getattr(self, field))
            target_model = bulk_models[field]
            self.bulk(df, target_model)

    # ----------------------------------------------------------------------
    def bulk(self, df, target_model):
        """"""
        if target_model.objects.count():
            actual = set([q[0] for q in target_model.objects.values_list('pk')])
        else:
            actual = set()

        incoming = set(df['pk'].to_list())

        to_create = incoming.difference(actual)
        to_update = actual.intersection(incoming)

        many_to_many = ['inventors']

        if to_create:
            elements = df.loc[df['pk'].isin(to_create)].to_dict('records')
            bulk = [target_model(**self.fix_arguments(element, target_model, to_ignore=many_to_many)) for element in elements]
            for m in many_to_many:
                [getattr(blk, m).set(json.loads(element[m])) for blk, element in zip(bulk, elements)]
            target_model.objects.bulk_create(bulk)

        if to_update:
            elements = df.loc[df['pk'].isin(to_update)].to_dict('records')
            bulk = [target_model(**self.fix_arguments(element, target_model, to_ignore=many_to_many)) for element in elements]

            fields = list(df.columns)
            for m in many_to_many:
                if m in [f.name for f in target_model._meta.fields]:
                    [getattr(blk, m).set(json.loads(element[m])) for blk, element in zip(bulk, elements)]
                if m in fields:
                    fields.remove(m)

            fields.remove('pk')
            target_model.objects.bulk_update(bulk, fields=fields)

    # ----------------------------------------------------------------------
    def fix_arguments(self, element, target_model, to_ignore=[]):
        """"""
        fields_in_dict = {field.name: dict([c[::-1] for c in field.choices]) for field in target_model._meta.fields if field.choices}
        for k in element:
            if k in fields_in_dict:
                if element[k] in fields_in_dict[k]:
                    element[k] = fields_in_dict[k][element[k]]
                else:
                    print(f'{element[k]} not in {k}')

        if 'leader' in element:
            element['leader'] = Professor.objects.get(pk=element['leader'])

        return {k: element[k] for k in element if not k in to_ignore}


########################################################################
class DatabasesBulk(Bulker, models.Model):
    """"""
    bulk_ResearchGroup = models.FileField('Research groups', null=True, blank=True)
    bulk_Professor = models.FileField('Professors', null=True, blank=True)
    bulk_Patent = models.FileField('Patents', null=True, blank=True)

    class Meta:
        verbose_name = "Update databases with CSV dataset"
