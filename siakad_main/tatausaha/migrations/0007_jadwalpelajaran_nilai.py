# Generated by Django 3.2 on 2021-04-26 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('murid', '0012_alter_murid_kelas'),
        ('tatausaha', '0006_auto_20210426_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nilai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.CharField(max_length=50, null=True)),
                ('id_mapel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tatausaha.mapel')),
                ('nis', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='murid.murid')),
            ],
        ),
        migrations.CreateModel(
            name='JadwalPelajaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kelas', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tatausaha.kelas')),
                ('id_mapel', models.ForeignKey(on_delete=django.db.models.deletion.RestrictedError, to='tatausaha.mapel')),
            ],
        ),
    ]