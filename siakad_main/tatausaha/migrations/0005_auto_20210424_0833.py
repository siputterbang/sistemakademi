# Generated by Django 3.2 on 2021-04-24 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murid', '0009_auto_20210424_0833'),
        ('tatausaha', '0004_alter_matapelajaran_guru_pengampu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kelas', models.CharField(max_length=5)),
                ('nama_kelas', models.CharField(max_length=5)),
                ('mata_pelajaran', models.CharField(max_length=50)),
                ('jam', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='MataPelajaran',
        ),
    ]