# Generated by Django 4.0.6 on 2022-07-19 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='primeiroNome',
            new_name='Nome',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='segundoNome',
            new_name='sobrenome',
        ),
    ]
