# Generated by Django 3.2 on 2021-04-24 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guru', '0002_auto_20210414_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='guru',
            name='kelas',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
