# Generated by Django 5.0 on 2024-05-04 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoportal', '0004_alter_monument_foundation_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monument',
            options={'verbose_name': "історична пам'ятка", 'verbose_name_plural': "історичні пам'ятки"},
        ),
    ]