# Generated by Django 4.1.6 on 2023-02-17 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_alter_user_email_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_doctor', to='receipts.doctor'),
        ),
    ]
