# Generated by Django 5.1.1 on 2024-10-09 12:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='token_created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='verification_token',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
    ]
