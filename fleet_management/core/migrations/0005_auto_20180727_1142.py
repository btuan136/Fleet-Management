# Generated by Django 2.0.6 on 2018-07-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_requisition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
