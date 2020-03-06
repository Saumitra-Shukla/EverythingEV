# Generated by Django 2.2 on 2020-03-06 09:56

from django.db import migrations, models
import django.db.models.deletion
import userapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0032_auto_20200306_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chargingstationrecord',
            name='elec_kwh',
        ),
        migrations.AddField(
            model_name='chargingstationrecord',
            name='consumer',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='recordof', to='userapp.Consumer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chargingstationrecord',
            name='duration',
            field=models.IntegerField(default=userapp.models.duration),
        ),
        migrations.AddField(
            model_name='chargingstationrecord',
            name='elec_consumption',
            field=models.IntegerField(default=userapp.models.cost),
        ),
        migrations.AddField(
            model_name='chargingstationrecord',
            name='vehicle',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='csvehicles', to='userapp.Vehicle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=30.706979, max_digits=9),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=76.760348, max_digits=9),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='price_kwh',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=5),
        ),
    ]
