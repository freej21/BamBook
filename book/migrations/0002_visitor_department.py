# Generated by Django 4.2.5 on 2023-09-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='department',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Human Resources', 'Human Resources'), ('DPWH', 'DPWH')], default='Engineering', max_length=20),
        ),
    ]