# Generated by Django 3.2.15 on 2022-12-09 08:04

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
            name='AutoAdminSingleton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='password')),
                ('password_hash', models.CharField(blank=True, max_length=128, null=True, verbose_name='password hash')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auto_admin_account', to=settings.AUTH_USER_MODEL, verbose_name='account')),
            ],
            options={
                'verbose_name': 'auto admin properties',
                'verbose_name_plural': 'auto admin properties',
            },
        ),
    ]
