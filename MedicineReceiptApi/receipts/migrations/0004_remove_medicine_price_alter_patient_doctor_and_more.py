# Generated by Django 4.1.6 on 2023-02-17 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0003_alter_patient_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='price',
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personal_doctor', to='receipts.doctor'),
        ),
        migrations.CreateModel(
            name='PharmacyMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipts.medicine')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipts.pharmacy')),
            ],
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='medicines',
            field=models.ManyToManyField(through='receipts.PharmacyMedicine', to='receipts.medicine'),
        ),
    ]