# Generated by Django 3.1 on 2020-10-14 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201014_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.subject'),
        ),
    ]
