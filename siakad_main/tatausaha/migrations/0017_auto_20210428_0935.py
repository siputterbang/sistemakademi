# Generated by Django 3.2 on 2021-04-28 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tatausaha', '0016_alter_jadwalpelajaran_hari'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapel',
            name='Jumlah_Pertemuan',
        ),
        migrations.AddField(
            model_name='jadwalpelajaran',
            name='Jumlah_Pertemuan',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='jadwalpelajaran',
            name='hari',
            field=models.CharField(choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')], default='Senin', max_length=7),
        ),
        migrations.AlterField(
            model_name='jadwalpelajaran',
            name='id_mapel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tatausaha.mapel'),
        ),
    ]
