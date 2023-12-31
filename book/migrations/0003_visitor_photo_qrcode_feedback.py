# Generated by Django 4.2.5 on 2023-09-05 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_visitor_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='visitor_photos/'),
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('visitor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.visitor')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')])),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.visitor')),
            ],
        ),
    ]
