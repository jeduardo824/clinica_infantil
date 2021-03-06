# Generated by Django 2.0 on 2018-01-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino')], max_length=10, null=True, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Telefone'),
        ),
    ]
