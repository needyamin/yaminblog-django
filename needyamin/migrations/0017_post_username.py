# Generated by Django 3.2.3 on 2021-07-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needyamin', '0016_auto_20210725_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
