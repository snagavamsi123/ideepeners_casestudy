# Generated by Django 3.2.5 on 2021-07-14 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IdeepApp', '0003_dailyupdate_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='Order_id',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
