# Generated by Django 3.2.15 on 2022-11-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dima', '0005_delete_internalcall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.CharField(help_text='Separated by comma', max_length=256, verbose_name='emails'),
        ),
        migrations.AlterField(
            model_name='team',
            name='ext',
            field=models.IntegerField(help_text='Separated by comma', verbose_name='extention'),
        ),
        migrations.AlterField(
            model_name='team',
            name='names',
            field=models.CharField(help_text='Separated by comma', max_length=256, verbose_name='names'),
        ),
    ]
