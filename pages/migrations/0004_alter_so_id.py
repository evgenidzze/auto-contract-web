# Generated by Django 4.2.3 on 2023-09-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='so',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
