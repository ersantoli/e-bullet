# Generated by Django 4.2.13 on 2024-06-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_boletim'),
    ]

    operations = [
        migrations.CreateModel(
            name='boletim2b',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matematica1b', models.CharField(max_length=2)),
                ('portugues1b', models.CharField(max_length=2)),
            ],
        ),
    ]