# Generated by Django 3.0.3 on 2020-07-10 11:08

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
            name='AlbumInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='标题')),
                ('introduce', models.CharField(blank=True, max_length=200, verbose_name='描述')),
                ('photo', models.ImageField(blank=True, upload_to='images/album/', verbose_name='图片')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '图片墙管理',
                'verbose_name_plural': '图片墙管理',
            },
        ),
    ]
