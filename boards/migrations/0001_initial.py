# Generated by Django 2.2.13 on 2020-12-26 19:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('avatar', models.URLField(max_length=512, null=True)),
                ('curator_name', models.CharField(max_length=120)),
                ('curator_title', models.CharField(max_length=120, null=True)),
                ('curator_url', models.TextField(null=True)),
                ('curator_bio', models.TextField(null=True)),
                ('curator_footer', models.TextField(null=True)),
                ('schema', models.TextField(null=True)),
                ('created_at', models.DateTimeField(db_index=True)),
                ('updated_at', models.DateTimeField()),
                ('refreshed_at', models.DateTimeField(null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_private', models.BooleanField(default=True)),
                ('index', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'boards',
                'ordering': ['index', 'name'],
            },
        ),
        migrations.CreateModel(
            name='BoardBlock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512, null=True)),
                ('slug', models.SlugField()),
                ('view', models.CharField(default='blocks/three.html', max_length=256)),
                ('created_at', models.DateTimeField(db_index=True)),
                ('updated_at', models.DateTimeField()),
                ('index', models.PositiveIntegerField(default=0)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='boards.Board')),
            ],
            options={
                'db_table': 'board_blocks',
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='BoardFeed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512, null=True)),
                ('comment', models.TextField(null=True)),
                ('url', models.TextField()),
                ('icon', models.URLField(max_length=512, null=True)),
                ('rss', models.URLField(max_length=512, null=True)),
                ('mix', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('view', models.CharField(default='feeds/simple.html', max_length=256)),
                ('created_at', models.DateTimeField(db_index=True)),
                ('last_article_at', models.DateTimeField(null=True)),
                ('refreshed_at', models.DateTimeField(null=True)),
                ('frequency', models.FloatField(default=0.0)),
                ('columns', models.SmallIntegerField(default=1)),
                ('articles_per_column', models.SmallIntegerField(default=15)),
                ('index', models.PositiveIntegerField(default=0)),
                ('conditions', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('is_parsable', models.BooleanField(default=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='boards.BoardBlock')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='boards.Board')),
            ],
            options={
                'db_table': 'board_feeds',
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('uniq_id', models.TextField(db_index=True)),
                ('url', models.URLField(max_length=2048)),
                ('type', models.CharField(max_length=16)),
                ('domain', models.CharField(max_length=256, null=True)),
                ('title', models.CharField(max_length=256)),
                ('image', models.URLField(max_length=512, null=True)),
                ('description', models.TextField(null=True)),
                ('summary', models.TextField(null=True)),
                ('created_at', models.DateTimeField(db_index=True)),
                ('updated_at', models.DateTimeField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='boards.Board')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='boards.BoardFeed')),
            ],
            options={
                'db_table': 'articles',
                'ordering': ['-created_at'],
            },
        ),
    ]
