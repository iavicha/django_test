# Generated by Django 3.1.1 on 2020-10-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(editable=False, max_length=20),
        ),
    ]
