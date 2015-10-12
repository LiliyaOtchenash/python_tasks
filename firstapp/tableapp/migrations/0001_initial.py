# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text_field', models.CharField(max_length=200)),
                ('decimal_field', models.DecimalField(decimal_places=3, max_digits=12)),
            ],
        ),
    ]
