# Generated by Django 5.1.4 on 2025-01-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Not completed', 'Not completed')], default='Notompleted', max_length=100),
        ),
    ]