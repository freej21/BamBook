# Generated by Django 4.2.6 on 2023-12-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0029_alter_averagefeedback_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='averagefeedback',
            name='average_rating',
            field=models.FloatField(null=True),
        ),
    ]
