# Generated by Django 4.2.5 on 2023-10-04 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
