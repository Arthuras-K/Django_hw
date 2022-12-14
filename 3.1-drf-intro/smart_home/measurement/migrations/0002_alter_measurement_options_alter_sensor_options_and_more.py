# Generated by Django 4.1.2 on 2022-11-23 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение', 'verbose_name_plural': 'Измерения'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
        migrations.AddField(
            model_name='measurement',
            name='photo',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id_sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
        ),
    ]
