# Generated by Django 5.2.1 on 2025-05-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_domicilio_informacaodomicilio'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacaoMorador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Morador')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('idade', models.PositiveIntegerField(verbose_name='Idade')),
            ],
        ),
    ]
