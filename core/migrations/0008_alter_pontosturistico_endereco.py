# Generated by Django 4.0 on 2022-01-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0007_remove_pontosturistico_endereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontosturistico',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
        ),
    ]
