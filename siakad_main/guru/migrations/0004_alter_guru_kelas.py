# Generated by Django 3.2 on 2021-04-24 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tatausaha', '0005_auto_20210424_0833'),
        ('guru', '0003_guru_kelas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guru',
            name='kelas',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tatausaha.kelas'),
        ),
    ]