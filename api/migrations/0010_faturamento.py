# Generated by Django 4.0.6 on 2022-07-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_concluido_pedido_pedido_concluido'),
    ]

    operations = [
        migrations.CreateModel(
            name='faturamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]