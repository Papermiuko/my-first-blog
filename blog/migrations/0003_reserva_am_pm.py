# Generated by Django 5.0.6 on 2024-05-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240516_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='am_pm',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=2),
        ),
    ]
