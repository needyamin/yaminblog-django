# Generated by Django 3.2.3 on 2021-07-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needyamin', '0015_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]