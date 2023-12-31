# Generated by Django 4.2.7 on 2023-11-01 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0008_cidade_alter_contato_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='bairro',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contato',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgendaApp.cidade'),
        ),
    ]
