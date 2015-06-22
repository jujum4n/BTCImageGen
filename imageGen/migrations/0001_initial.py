# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitcoinInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('price', models.FloatField()),
                ('last_checked', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
