# Generated by Django 5.0.6 on 2024-06-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_complaint_complaint_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
