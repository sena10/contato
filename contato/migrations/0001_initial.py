# Generated by Django 4.2.5 on 2023-09-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('info', models.TextField(blank=True, verbose_name='Informações')),
                ('whatsapp', models.CharField(blank=True, max_length=15, verbose_name='Whatsapp')),
                ('endereco', models.CharField(blank=True, max_length=200, verbose_name='Endereço')),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares', verbose_name='Avatar')),
            ],
        ),
    ]
