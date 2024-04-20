# Generated by Django 5.0.2 on 2024-04-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_achievementprogress_doneornot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='scores',
        ),
        migrations.AddField(
            model_name='achievement',
            name='addExperience',
            field=models.IntegerField(blank=True, null=True, verbose_name='Выдаваемый опыт'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='addScore',
            field=models.IntegerField(blank=True, null=True, verbose_name='Выдаваемыe баллы'),
        ),
    ]
