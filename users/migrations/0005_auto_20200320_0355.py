# Generated by Django 3.0.4 on 2020-03-20 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200319_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='message',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]