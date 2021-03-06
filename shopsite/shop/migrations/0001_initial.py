# Generated by Django 2.2.6 on 2019-10-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('normal', 'Normal'), ('deleted', 'Deleted'), ('banned', 'Banned'), ('popular', 'Popular')], db_index=True, default='normal', max_length=10, verbose_name='store_status')),
                ('store_name', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='store name')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('store_location', models.CharField(db_index=True, max_length=200, verbose_name='store location')),
                ('store_fans', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'store',
                'verbose_name_plural': 'stores',
                'ordering': ('store_name',),
            },
        ),
    ]
