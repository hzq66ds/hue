# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 18:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_design', models.BooleanField(db_index=True, default=True, help_text='If the document is not a submitted job but a real query, script, workflow.', verbose_name='Is a user document, not a document submission.')),
            ],
        ),
        migrations.CreateModel(
            name='PigScript',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pig.Document')),
                ('data', models.TextField(default=b'{"name": "", "parameters": [], "script": "", "hadoopProperties": [], "properties": [], "resources": [], "job_id": null}')),
            ],
            bases=('pig.document',),
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(help_text='User who can modify the job.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]