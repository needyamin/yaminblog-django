# Generated by Django 3.2.3 on 2021-07-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needyamin', '0013_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
