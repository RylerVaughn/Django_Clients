# Generated by Django 5.1.6 on 2025-02-06 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_clientrelations'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contact',
            field=models.CharField(default='NaN', max_length=15),
        ),
        migrations.DeleteModel(
            name='ClientRelations',
        ),
    ]
