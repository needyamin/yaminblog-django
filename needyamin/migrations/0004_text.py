# Generated by Django 3.2.3 on 2021-07-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needyamin', '0003_auto_20210717_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
