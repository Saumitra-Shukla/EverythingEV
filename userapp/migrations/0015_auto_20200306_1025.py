# Generated by Django 2.2 on 2020-03-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_chargingstationrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='battery_capacity',
            new_name='battery_type',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='name',
            new_name='horsepower',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='type4or2',
            field=models.IntegerField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_range',
            field=models.IntegerField(),
        ),
    ]