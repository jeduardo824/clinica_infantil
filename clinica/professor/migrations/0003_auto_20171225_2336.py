# Generated by Django 2.0 on 2017-12-26 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_auto_20171219_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='genero',
        ),
        migrations.AddField(
            model_name='professor',
            name='sexo',
            field=models.CharField(choices=[(0, 'Feminino'), (1, 'Masculino')], max_length=1, null=True, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='cpf',
            field=models.CharField(max_length=11, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=30, null=True, verbose_name='Nome'),
        ),
    ]