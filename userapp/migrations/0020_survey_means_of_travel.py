# Generated by Django 3.0.5 on 2020-06-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0019_survey_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='means_of_travel',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Ambulance', 'Ambulance'), ('Private Authority', 'Private Authority'), ('Goverment', 'Goverment'), ('Tours and Travel', 'Tours and Travel'), ('Goods Carrier', 'Goods Carrier')], default='', max_length=20),
        ),
    ]