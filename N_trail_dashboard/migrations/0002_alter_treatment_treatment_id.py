# Generated by Django 5.0.6 on 2024-05-31 06:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('N_trail_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='Treatment_ID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
