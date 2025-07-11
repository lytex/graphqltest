# Generated by Django 5.2.4 on 2025-07-03 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('plan', models.IntegerField(choices=[(0, 'Hobby Plan'), (1, 'Pro Plan')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.user')),
            ],
        ),
    ]
