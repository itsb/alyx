# Generated by Django 2.1.4 on 2019-01-24 10:25

from django.db import migrations, models
import django.db.models.deletion
import misc.models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0002_auto_20181119_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lablocation',
            name='lab',
            field=models.ForeignKey(default=misc.models.default_lab, on_delete=django.db.models.deletion.CASCADE, to='misc.Lab'),
        ),
    ]
