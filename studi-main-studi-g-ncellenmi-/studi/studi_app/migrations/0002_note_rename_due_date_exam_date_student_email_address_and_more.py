# Generated by Django 5.0.4 on 2024-05-28 04:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studi_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='due_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='student',
            name='email_address',
            field=models.EmailField(default=2, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='schedule',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
