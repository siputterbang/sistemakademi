# Generated by Django 3.2 on 2021-04-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatausaha', '0004_alter_matapelajaran_guru_pengampu'),
        ('murid', '0007_remove_ruangan_siswadiruangan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='murid',
            name='Mata_Pelajaran',
        ),
        migrations.AddField(
            model_name='murid',
            name='Mata_Pelajaran',
            field=models.ManyToManyField(to='tatausaha.MataPelajaran'),
        ),
    ]