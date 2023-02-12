# Generated by Django 4.1.6 on 2023-02-12 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=300)),
                ('price', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'medicine',
            },
        ),
    ]
