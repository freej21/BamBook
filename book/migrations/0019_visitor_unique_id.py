# Generated by Django 4.2.6 on 2023-11-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_delete_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='unique_id',
            field=models.UUIDField(blank=True, editable=False, null=True, unique=True),
        ),
    ]