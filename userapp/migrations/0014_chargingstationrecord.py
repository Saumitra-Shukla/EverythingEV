# Generated by Django 2.2 on 2020-03-05 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_delete_chargingstationrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargingStationRecord',
            fields=[
                ('cs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='userapp.ChargingStation')),
                ('starttime', models.TimeField(default='00:00:00')),
                ('stoptime', models.TimeField(default='00:00:00')),
                ('elec_kwh', models.DecimalField(decimal_places=6, max_digits=9)),
                ('consumer_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userVehicles', to='userapp.Consumer')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='csvehicles', to='userapp.Vehicle')),
            ],
        ),
    ]