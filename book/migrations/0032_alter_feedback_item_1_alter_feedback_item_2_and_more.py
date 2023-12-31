# Generated by Django 4.2.6 on 2023-12-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0031_alter_averagefeedback_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='item_1',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_2',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_3',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_4',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_5',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_6',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_7',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_8',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_9',
            field=models.DecimalField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], decimal_places=2, max_digits=3, null=True),
        ),
    ]
