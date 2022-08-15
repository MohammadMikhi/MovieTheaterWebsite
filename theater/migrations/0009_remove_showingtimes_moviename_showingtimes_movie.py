# Generated by Django 4.0.6 on 2022-08-06 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0008_alter_bookings_bookingclass_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showingtimes',
            name='movieName',
        ),
        migrations.AddField(
            model_name='showingtimes',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theater.movies'),
        ),
    ]