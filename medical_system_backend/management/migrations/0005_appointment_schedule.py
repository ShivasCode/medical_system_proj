# Generated by Django 3.2 on 2023-07-02 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.schedule'),
        ),
    ]
