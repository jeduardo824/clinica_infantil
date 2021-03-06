# Generated by Django 2.0 on 2018-01-10 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crianca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, null=True)),
                ('naturalidade', models.CharField(max_length=30, null=True)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino')], max_length=12)),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone:')),
                ('nome_mae', models.CharField(max_length=30, verbose_name='Nome da Mãe:')),
                ('nome_pai', models.CharField(max_length=30, verbose_name='Nome do Pai:')),
                ('rua', models.CharField(max_length=30, null=True)),
                ('bairro', models.CharField(max_length=30, null=True)),
                ('cep', models.CharField(max_length=10, null=True)),
                ('cidade', models.CharField(max_length=20, null=True)),
                ('estado', models.CharField(choices=[('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapa', 'Amapa'), ('Amazonas', 'Amazonas'), ('Bahia', 'Bahia'), ('Ceara', 'Ceara'), ('Distrito Federal', 'Distrito Federal'), ('Espirito Santo', 'Espirito Santo'), ('Goias', 'Goias'), ('Maranhao', 'Maranhao'), ('Mato Grosso', 'Mato Grosso'), ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'), ('Para', 'Para'), ('Paraiba', 'Paraiba'), ('Parana', 'Parana'), ('Pernambuco', 'Pernambuco'), ('Piaui', 'Piaui'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rio Grande do Norte', 'Rio Grande do Norte'), ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Rondonia', 'Rondonia'), ('Roraima', 'Roraima'), ('Santa Catarina', 'Santa Catarina'), ('Sao Paulo', 'Sao Paulo'), ('Sergipe', 'Sergipe'), ('Tocantins', 'Tocantins')], max_length=30, null=True)),
                ('zona', models.CharField(blank=True, choices=[('Zona Norte', 'Norte'), ('Zona Leste', 'Leste'), ('Zona Sul', 'Sul'), ('Zona Sudeste', 'Sudeste'), ('Centro', 'Centro')], max_length=10, null=True)),
                ('facebook', models.CharField(blank=True, max_length=30, null=True)),
                ('instagram', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('renda_familia', models.IntegerField(null=True)),
                ('numero_pessoas_casa', models.IntegerField(null=True)),
                ('renda_percapita', models.FloatField(null=True)),
                ('escolaridade_pai', models.CharField(choices=[('Primario Incompleto', 'Primário Incompleto'), ('Primario Completo', 'Primário Completo'), ('Ginasio Incompleto', 'Ginásio Incompleto'), ('Ginasio Completo', 'Ginásio Completo'), ('2 Grau Incompleto AcadEmico', '2º Grau Incompleto Acadêmico'), ('2 Grau Completo Academico', '2º Grau Completo Acadêmico'), ('2 Grau Incompleto Tecnico', '2º Grau Incompleto Técnico'), ('2 Grau Completo Tecnico', '2º Grau Completo Técnico'), ('3 Grau Incompleto', '3º Grau Incompleto'), ('3 Grau Completo', '3º Grau Completo'), ('Pos Graduacao ou Especializacao Cursando', 'Pós Grad./Espec. Cursando'), ('Pos Graduacao ou Especializacao Concluido', 'Pós Grad./Espec. Concluído'), ('Mestrado Cursando', 'Mestrado Cursando'), ('Mestrado Concluido', 'Mestrado Concluído'), ('Doutorado Cursando', 'Doutorado Cursando'), ('Doutorado Concluido', 'Doutorado Concluído'), ('MBA Cursando', 'MBA Cursando'), ('MBA ConcluIdo', 'MBA Concluído')], max_length=220, null=True)),
                ('escolaridade_mae', models.CharField(choices=[('Primario Incompleto', 'Primário Incompleto'), ('Primario Completo', 'Primário Completo'), ('Ginasio Incompleto', 'Ginásio Incompleto'), ('Ginasio Completo', 'Ginásio Completo'), ('2 Grau Incompleto AcadEmico', '2º Grau Incompleto Acadêmico'), ('2 Grau Completo Academico', '2º Grau Completo Acadêmico'), ('2 Grau Incompleto Tecnico', '2º Grau Incompleto Técnico'), ('2 Grau Completo Tecnico', '2º Grau Completo Técnico'), ('3 Grau Incompleto', '3º Grau Incompleto'), ('3 Grau Completo', '3º Grau Completo'), ('Pos Graduacao ou Especializacao Cursando', 'Pós Grad./Espec. Cursando'), ('Pos Graduacao ou Especializacao Concluido', 'Pós Grad./Espec. Concluído'), ('Mestrado Cursando', 'Mestrado Cursando'), ('Mestrado Concluido', 'Mestrado Concluído'), ('Doutorado Cursando', 'Doutorado Cursando'), ('Doutorado Concluido', 'Doutorado Concluído'), ('MBA Cursando', 'MBA Cursando'), ('MBA ConcluIdo', 'MBA Concluído')], max_length=220, null=True)),
                ('prof_pai', models.CharField(max_length=30, null=True)),
                ('prof_mae', models.CharField(max_length=30, null=True)),
                ('responsavel', models.CharField(choices=[('Mae', 'Mãe'), ('Pai', 'Pai'), ('Avos', 'Avós'), ('Outro Parente', 'Outro parente'), ('Baba', 'Babá'), ('Outra pessoa', 'Outra pessoa')], max_length=30)),
                ('mora_pais', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10)),
                ('nasceu_tempo', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=40)),
                ('nasceu_tempo_meses', models.IntegerField(blank=True, default=9)),
                ('nasceu_tempo_semanas', models.IntegerField(blank=True, default=40)),
                ('peso_ao_nascer', models.CharField(choices=[('Menor que 2.500', 'Menor que 2.500'), ('Entre 2.500 e 3000', 'Entre 2.500 e 3000'), ('Entre 3.000 e 3.500', 'Entre 3.000 e 3.500'), ('Mais que 4.500', 'Mais que 4.500'), ('Nao Lembra', ' Não Lembra')], max_length=30)),
                ('visita_prenatal', models.CharField(choices=[('0', 'Nao fez/Nao Lembra'), ('1 a 3', 'De 1 a 3 visitas'), ('3 a 6', 'De 3 a 6 visitas'), ('6 a 9', 'De 6 a 9 visitas'), ('Mais de 9', 'Mais de 9 visitas')], max_length=100)),
                ('data_cadastro', models.DateField(null=True, verbose_name='Data do cadastro:')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
