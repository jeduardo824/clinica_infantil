# Generated by Django 2.0 on 2018-01-11 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crianca', '0007_auto_20180111_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crianca',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]