# Generated by Django 4.2.2 on 2023-08-26 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0002_alter_cardmodel_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
