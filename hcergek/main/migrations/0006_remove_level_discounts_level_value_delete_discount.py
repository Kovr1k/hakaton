# Generated by Django 5.0.2 on 2024-04-20 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_userachievementnotcomplate_achievementnotcomplate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='discounts',
        ),
        migrations.AddField(
            model_name='level',
            name='value',
            field=models.IntegerField(default=0, verbose_name='Значение(%)'),
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
