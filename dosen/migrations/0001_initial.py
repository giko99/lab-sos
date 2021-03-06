# Generated by Django 2.2 on 2020-09-30 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=100)),
                ('nama_dosen', models.CharField(max_length=100)),
                ('fakultas', models.CharField(max_length=100)),
                ('jurusan', models.CharField(max_length=100)),
                ('kelompok', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dosen', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
