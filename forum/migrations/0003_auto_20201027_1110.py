# Generated by Django 2.2 on 2020-10-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20201014_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komen',
            name='posting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentar', to='forum.Posting'),
        ),
    ]
