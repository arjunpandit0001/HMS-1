# Generated by Django 2.0 on 2020-06-19 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient_details', '0008_auto_20200618_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=20)),
                ('payment_for', models.CharField(max_length=30)),
                ('cost', models.CharField(max_length=7)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient_details.patient_appointment')),
            ],
        ),
    ]
