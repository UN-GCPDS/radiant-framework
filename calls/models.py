from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from datetime import date
import random
import os

upload_to_internal_call = os.path.join('uploads', 'calls_internal')
upload_to_external_call = os.path.join('uploads', 'calls_external')


########################################################################
class InternalCall(models.Model):
    """"""
    image = models.FileField('call', upload_to=upload_to_internal_call, blank=True, null=True)
    expiration = models.DateField('expiration')
    link = models.URLField('link')
    title = models.CharField('title', max_length=2 ** 10)
    active = models.BooleanField('active', default=True)

    @property
    # ----------------------------------------------------------------------
    def color(self):
        """"""
        return random.choice([
            '#CCA529',
            '#B45C18',
            '#341B4D',
            '#135714',
            '#67160E',
            '#153465',
        ])

    @property
    # ----------------------------------------------------------------------
    def expired(self):
        return not (self.active and date.today() < self.expiration.date())


########################################################################
class JointCall(models.Model):
    """"""
    image = models.FileField('call', upload_to=upload_to_internal_call, blank=True, null=True)
    expiration = models.DateField('expiration')
    link = models.URLField('link')
    title = models.CharField('title', max_length=2 ** 10)
    objective = models.TextField('objective', max_length=2 ** 12)
    headed = models.TextField('headed', max_length=2 ** 12)

    active = models.BooleanField('active', default=True)

    @property
    # ----------------------------------------------------------------------
    def color(self):
        """"""
        return random.choice([
            '#CCA529',
            '#B45C18',
            '#341B4D',
            '#135714',
            '#67160E',
            '#153465',
        ])

    @property
    # ----------------------------------------------------------------------
    def expired(self):
        return not (self.active and date.today() < self.expiration.date())


########################################################################
class Timeline(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='timeline', on_delete=models.CASCADE)
    activity = models.CharField('activity', max_length=2 ** 10)
    date = models.DateField('date')
    end_date = models.DateField('finalization date', blank=True, null=True)


########################################################################
class Doc(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='doc', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    doc = models.FileField('doc', upload_to=upload_to_internal_call, blank=True, null=True)


########################################################################
class Annex(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='annex', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    annex = models.FileField('annex', upload_to=upload_to_internal_call, blank=True, null=True)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=InternalCall)
def on_post_delete_internalcall(sender, instance, **kwargs):
    """"""
    for object_ in ['call']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)

