# Generated by Django 2.2.8 on 2020-01-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_boardfeed_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='curator_bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='curator_url',
            field=models.TextField(null=True),
        ),
    ]