# Generated by Django 4.2.6 on 2023-11-14 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_feedback_visitor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QRCode',
        ),
    ]
