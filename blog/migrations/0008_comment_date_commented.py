# Generated by Django 2.2.1 on 2019-06-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190616_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_commented',
            field=models.DateTimeField(auto_now=True),
        ),
    ]