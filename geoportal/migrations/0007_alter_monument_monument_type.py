# Generated by Django 5.0 on 2024-05-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoportal', '0006_alter_monument_monument_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monument',
            name='monument_type',
            field=models.CharField(choices=[('history', "Історичні об'єкти культурної спадщини"), ('architecture', 'Споруди культового призначення'), ('archeology', "Археологічні об'єкти культурної спадщини"), ('reservation', 'Державні історико-культурні заповідники та музеї')], max_length=50, verbose_name='Тип'),
        ),
    ]
