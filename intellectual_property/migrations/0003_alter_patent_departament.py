# Generated by Django 3.2.15 on 2022-11-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intellectual_property', '0002_rename_filing_patent_filling_alter_patent_inventors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='departament',
            field=models.CharField(choices=[('departament_0001', 'Departamento de administración'), ('departament_0002', 'Departamento de ciencias humanas'), ('departament_0003', 'Departamento de física y química'), ('departament_0004', 'Departamento de informática y computación'), ('departament_0005', 'Departamento de ingeniería civil'), ('departament_0006', 'Departamento de ingeniería eléctrica, electrónica y computación'), ('departament_0007', 'Departamento de ingeniería industrial'), ('departament_0008', 'Departamento de ingeniería química'), ('departament_0009', 'Departamento de matemáticas'), ('departament_0010', 'Escuela de arquitectura y urbanismo')], max_length=116, verbose_name='Departament'),
        ),
    ]
