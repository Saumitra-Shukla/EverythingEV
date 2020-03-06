# Generated by Django 2.2 on 2020-03-06 15:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import userapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_consumer', models.BooleanField(default=False, verbose_name='consumer status')),
                ('is_provider', models.BooleanField(default=False, verbose_name='provider status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ChargingStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=userapp.models.csnames, max_length=100)),
                ('city', models.CharField(default='city', max_length=100)),
                ('suburb', models.CharField(default='suburb', max_length=100)),
                ('lat', models.DecimalField(decimal_places=6, default=0.0, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, default=0.0, max_digits=9)),
                ('no_of_ports', models.IntegerField(default=userapp.models.portscount)),
                ('available_ports', models.IntegerField(default=0)),
                ('fast_dc', models.IntegerField(default=userapp.models.fasports)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('slow_ac', models.IntegerField(default=userapp.models.slowports)),
                ('price_kwh', models.DecimalField(decimal_places=2, default=12, max_digits=5)),
                ('restroom', models.BooleanField(default=False)),
                ('cctv', models.BooleanField(default=True)),
                ('opening_time', models.TimeField(default=userapp.models.starttime)),
                ('closing_time', models.TimeField(default=userapp.models.stoptime)),
                ('image', models.ImageField(null=True, upload_to='station_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('type4or2', models.IntegerField()),
                ('horsepower', models.CharField(max_length=100)),
                ('vehicle_range', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=6, max_digits=9)),
                ('battery_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('have_vehicle', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=10)),
                ('city', models.CharField(choices=[('None', 'None'), ('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Hyderabad', 'Hyderabad')], default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CsReport',
            fields=[
                ('cs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='userapp.ChargingStation')),
                ('time', models.DateField(default=userapp.models.randomdate)),
                ('t0', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t1', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t2', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t3', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t4', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t5', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t6', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t7', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t8', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t9', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t10', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t11', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t12', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t13', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t14', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t15', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t16', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t17', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t18', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t19', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t20', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t21', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t22', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t23', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t24', models.IntegerField(default=userapp.models.randomvehicles)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('business_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='provider_pics')),
            ],
        ),
        migrations.CreateModel(
            name='ChargingStationRecord',
            fields=[
                ('cs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='userapp.ChargingStation')),
                ('duration', models.IntegerField(default=userapp.models.duration)),
                ('elec_consumption', models.IntegerField(default=userapp.models.cost)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recordof', to='userapp.Consumer')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='csvehicles', to='userapp.Vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='chargingstation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownerof', to='userapp.Provider'),
        ),
    ]
