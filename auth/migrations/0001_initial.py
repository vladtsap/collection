# Generated by Django 2.2.8 on 2020-01-05 13:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=256, unique=True)),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=32, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'sessions',
            },
        ),
    ]
