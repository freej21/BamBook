# Generated by Django 4.2.6 on 2023-12-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0022_alter_feedback_item_1_alter_feedback_item_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='item_1',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_2',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_3',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_4',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_5',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_6',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_7',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_8',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='item_9',
            field=models.IntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree'), (0, 'N/A')], null=True),
        ),
    ]