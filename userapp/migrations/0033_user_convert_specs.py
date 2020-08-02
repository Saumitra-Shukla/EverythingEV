# Generated by Django 3.0.5 on 2020-08-02 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0032_auto_20200731_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_convert_specs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fully_electric', models.BooleanField(default=True)),
                ('vehicle_type', models.CharField(choices=[('3 wheeler', '3 wheeler'), ('mini SUV', 'mini SUV'), ('SUV', 'SUV'), ('Sedan', 'Sendan'), ('Heavy', 'Heavy')], default='', max_length=20)),
                ('price_range', models.IntegerField(choices=[('Below 5', 'Below 5'), ('5 to 7.5', '5 to 7.5'), ('above 7', 'above 7')], default=0)),
                ('dtd_sercive', models.BooleanField(default=False)),
            ],
        ),
    ]
