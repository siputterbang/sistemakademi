# Generated by Django 3.2 on 2021-04-26 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatausaha', '0007_jadwalpelajaran_nilai'),
    ]

    operations = [
        migrations.AddField(
            model_name='jadwalpelajaran',
            name='jam_pelajaran',
            field=models.CharField(max_length=50, null=True),
        ),
    ]