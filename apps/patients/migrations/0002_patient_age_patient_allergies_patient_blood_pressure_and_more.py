# Generated by Django 5.1.7 on 2025-03-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='allergies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_pressure',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB-')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='cholesterol_level',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='current_condition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='glucose_level',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='heart_rate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='medications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
