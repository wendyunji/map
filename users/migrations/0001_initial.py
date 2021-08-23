<<<<<<< HEAD
# Generated by Django 3.2.6 on 2021-08-21 20:22
=======
# Generated by Django 3.2.6 on 2021-08-20 17:23
>>>>>>> 357cc9a85f1f9b3c9f2cb1ccab8d70f828eed2b9

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship', models.CharField(max_length=30, null=True)),
                ('ship_name', models.CharField(max_length=40, null=True)),
                ('tonnage', models.CharField(max_length=30, null=True)),
                ('month', models.IntegerField(null=True)),
                ('active_sea', models.CharField(max_length=30, null=True)),
                ('time_f', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
