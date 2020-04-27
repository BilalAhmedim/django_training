# Generated by Django 3.0.5 on 2020-04-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeaturedApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredapp',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='featuredapp',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='featuredapp',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
