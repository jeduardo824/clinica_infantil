# Generated by Django 2.0 on 2018-01-16 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exame', '0007_auto_20180116_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnese',
            name='quando_nao_aceita',
            field=models.CharField(blank=True, choices=[('Insiste', 'Insiste'), ('Dessite', 'Desiste')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='anquiloglossia',
            field=models.CharField(choices=[('Nao permitiu Avaliar', 'Não permitiu Avaliar'), ('Inconclusivo', 'Inconclusivo'), ('Sim', 'Sim'), ('Nao', 'Não')], max_length=30),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_51',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_52',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_53',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_54',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_55',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_61',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_62',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_63',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_64',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_65',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_71',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_72',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_73',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_74',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_75',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_81',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_82',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_83',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_84',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='dente_85',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('G', 'G'), ('S', 'S'), ('C', 'C'), ('A', 'A'), ('DEE', 'DEE'), ('MB', 'MB'), ('T', 'T'), ('R', 'R')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='lingua',
            field=models.CharField(choices=[('Sulcada', 'Sulcada'), ('Outro', 'Outro'), ('Geografica', 'Geográfica'), ('Normal', 'Normal')], max_length=15),
        ),
        migrations.AlterField(
            model_name='exameclinicocomdentes',
            name='tecidos_moles',
            field=models.CharField(choices=[('Alterado', 'Alterado'), ('Normal', 'Normal')], max_length=20),
        ),
        migrations.AlterField(
            model_name='exameclinicosemdentes',
            name='anquiloglossia',
            field=models.CharField(choices=[('Nao permitiu Avaliar', 'Não permitiu Avaliar'), ('Inconclusivo', 'Inconclusivo'), ('Sim', 'Sim'), ('Nao', 'Não')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicosemdentes',
            name='lingua',
            field=models.CharField(choices=[('Sulcada', 'Sulcada'), ('Outro', 'Outro'), ('Geografica', 'Geográfica'), ('Normal', 'Normal')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='exameclinicosemdentes',
            name='tecido_mole',
            field=models.CharField(choices=[('Alterado', 'Alterado'), ('Normal', 'Normal')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='primeiraconsultacomdentes',
            name='classificacao_boca_mae',
            field=models.CharField(choices=[('Mae nao presente', 'Mae nao esta presente'), ('Boa', 'Boa'), ('Ruim', 'Ruim'), ('Regular', 'Regular')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='primeiraconsultacomdentes',
            name='hb_ao_dia',
            field=models.CharField(choices=[('1 vez ao dia', '1 vez ao dia'), ('3 vezes ao dia', '3 vezes ao dia'), ('Mais de 4 vezes ao dia', 'Mais de 4 vezes ao dia'), ('4 vezes ao dia', '4 vezes ao dia'), ('2 vezes ao dia', '2 vezes ao dia')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='primeiraconsultacomdentes',
            name='ingere_guloseimas',
            field=models.CharField(blank=True, choices=[('Livremente', 'Livremente'), ('Raramente', 'Raramente'), ('3x por Semana', 'Até 3x por Semana'), ('Nunca', 'Nunca')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='primeiraconsultacomdentes',
            name='irrompeu_dente',
            field=models.CharField(choices=[('Nasceu com dente', 'Nasceu com dente'), ('Nao lembra', 'Nao lembra'), ('Informar Idade', 'Informar Idade')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='primeiraconsultacomdentes',
            name='mama',
            field=models.CharField(blank=True, choices=[('Mamadeira', 'Mamadeira'), ('Peito', 'Peito')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='primeiraconsultacomdentes',
            name='quando_nao_aceita',
            field=models.CharField(blank=True, choices=[('Insiste', 'Insiste'), ('Dessite', 'Desiste')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='primeiraconsultasemdentes',
            name='classificacao_boca_mae',
            field=models.CharField(choices=[('Mae nao presente', 'Mae nao esta presente'), ('Boa', 'Boa'), ('Ruim', 'Ruim'), ('Regular', 'Regular')], max_length=16, null=True),
        ),
    ]
