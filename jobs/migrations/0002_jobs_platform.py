# Generated by Django 3.2.3 on 2021-05-18 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='platform',
            field=models.CharField(choices=[('desktop', 'Desktop App'), ('web', 'Web App')], max_length=100, null=True),
        ),
    ]
