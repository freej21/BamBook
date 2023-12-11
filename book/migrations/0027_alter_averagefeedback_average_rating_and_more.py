# Generated by Django 4.2.6 on 2023-12-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0026_averagefeedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='averagefeedback',
            name='average_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='averagefeedback',
            unique_together={('item_number',)},
        ),
    ]