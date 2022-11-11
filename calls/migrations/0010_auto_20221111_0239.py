# Generated by Django 3.2.15 on 2022-11-11 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0009_annexs_resultss_studentscall_termsofreferences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='name')),
                ('results', models.FileField(blank=True, null=True, upload_to='uploads/calls_internal', verbose_name='result')),
                ('joint_call', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='calls.jointcall')),
            ],
        ),
        migrations.AlterModelOptions(
            name='annexs',
            options={'verbose_name': 'Annex'},
        ),
        migrations.AlterModelOptions(
            name='results',
            options={'verbose_name': 'Result'},
        ),
        migrations.AlterModelOptions(
            name='termsofreferences',
            options={'verbose_name': 'TermsOfReference'},
        ),
        migrations.AlterField(
            model_name='results',
            name='joint_call',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='calls.studentscall'),
        ),
        migrations.AlterField(
            model_name='studentscall',
            name='economic_stimulus',
            field=models.CharField(max_length=4096, verbose_name='economic_stimulus'),
        ),
        migrations.AlterField(
            model_name='studentscall',
            name='supervise',
            field=models.CharField(max_length=4096, verbose_name='supervise'),
        ),
        migrations.DeleteModel(
            name='ResultsS',
        ),
    ]
