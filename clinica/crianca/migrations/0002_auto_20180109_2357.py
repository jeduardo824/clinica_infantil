# Generated by Django 2.0 on 2018-01-10 01:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crianca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crianca',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
