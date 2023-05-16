# Generated by Django 4.2 on 2023-05-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_orders_remove_students_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='discount',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='place_at',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]