# Generated by Django 4.2.6 on 2023-12-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0035_visitor_time_in_visitor_time_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='captured_photo',
            field=models.ImageField(default='image.png', upload_to='captured_visitor_photos/'),
        ),
    ]
