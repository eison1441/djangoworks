# Generated by Django 5.1.5 on 2025-01-29 05:53

import django.db.models.deletion
import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0006_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', embed_video.fields.EmbedVideoField(null=True)),
                ('order', models.PositiveIntegerField()),
                ('module_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='instructor.module')),
            ],
        ),
    ]
