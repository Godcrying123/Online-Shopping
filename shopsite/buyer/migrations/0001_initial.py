# Generated by Django 2.2.6 on 2019-10-23 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.User')),
                ('status_vip', models.CharField(blank=True, choices=[('vip', 'VIP'), ('not-vip', 'Not VIP')], db_index=True, default='not-vip', max_length=10, verbose_name='status_vip')),
                ('status_user', models.CharField(blank=True, choices=[('normal', 'Normal'), ('deleted', 'Deleted'), ('banned', 'Banned')], db_index=True, default='normal', max_length=10, verbose_name='status_user')),
            ],
            options={
                'verbose_name': 'buyer',
                'ordering': ('username',),
            },
            bases=('user.user',),
        ),
    ]
