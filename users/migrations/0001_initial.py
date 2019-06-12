# Generated by Django 2.2.1 on 2019-05-29 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('description', models.CharField(max_length=500)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Ч', 'Чоловік'), ('Ж', 'Жінка')], default='Ч', max_length=1)),
                ('skills', models.CharField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]