# Generated by Django 5.2.4 on 2025-07-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='plan',
            field=models.CharField(choices=[('hobby', 'Hobby Plan'), ('pro', 'Pro plan')], default=0),
        ),
    ]
