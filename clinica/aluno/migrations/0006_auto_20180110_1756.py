# Generated by Django 2.0 on 2018-01-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0005_auto_20180110_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
