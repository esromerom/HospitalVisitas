# Generated by Django 2.0.3 on 2018-03-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiloperario',
            name='telefono',
            field=models.BigIntegerField(default=0),
        ),
    ]
