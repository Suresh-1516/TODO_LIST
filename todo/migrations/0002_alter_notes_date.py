# Generated by Django 4.1.7 on 2023-06-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
