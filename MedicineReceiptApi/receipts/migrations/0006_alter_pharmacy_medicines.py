# Generated by Django 4.1.6 on 2023-02-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0005_alter_pharmacymedicine_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='medicines',
            field=models.ManyToManyField(blank=True, null=True, through='receipts.PharmacyMedicine', to='receipts.medicine'),
        ),
    ]