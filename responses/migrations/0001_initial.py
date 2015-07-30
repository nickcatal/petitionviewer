# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='Petition Title')),
                ('url', models.URLField(verbose_name='Petition URL')),
                ('signatures', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at', '-signatures'],
                'verbose_name': 'Petition',
                'verbose_name_plural': 'Petitions',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=250)),
                ('title', models.CharField(max_length=250, verbose_name='Response Title')),
                ('total_signatures', models.IntegerField(verbose_name='Total Signatures')),
                ('response', models.TextField(verbose_name='Full White House Response')),
                ('url', models.CharField(max_length=250, verbose_name='Whitehouse URL')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at', '-total_signatures'],
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
            },
        ),
        migrations.AddField(
            model_name='petition',
            name='response',
            field=models.ForeignKey(to='responses.Response'),
        ),
    ]
