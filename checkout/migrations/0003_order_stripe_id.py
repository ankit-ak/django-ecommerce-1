# Generated by Django 2.2.12 on 2020-04-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200419_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]