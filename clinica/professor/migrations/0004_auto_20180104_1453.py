# Generated by Django 2.0 on 2018-01-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0003_auto_20171225_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='sexo',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino')], max_length=1, null=True, verbose_name='Sexo'),
        ),
    ]
