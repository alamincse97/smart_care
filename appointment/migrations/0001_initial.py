# Generated by Django 4.2.4 on 2024-08-18 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0003_review'),
        ('patient', '0002_alter_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_types', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=10)),
                ('appointment_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Running', 'Running')], default='Pending', max_length=10)),
                ('symptom', models.TextField()),
                ('cancel', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime')),
            ],
        ),
    ]
