# Generated by Django 2.2.6 on 2019-10-23 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='name')),
                ('username', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='username')),
                ('mail', models.EmailField(db_index=True, max_length=200, verbose_name='mail')),
                ('telephone', models.CharField(blank=True, max_length=100, verbose_name='telephone')),
                ('password', models.CharField(max_length=200, verbose_name='password')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated_time')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('username',),
                'index_together': {('username', 'mail')},
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='user.User')),
            ],
            options={
                'verbose_name': 'user token table',
                'verbose_name_plural': 'user token table',
                'db_table': 'user_token',
            },
        ),
        migrations.CreateModel(
            name='UserInfoEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='name')),
                ('recaddress', models.CharField(blank=True, max_length=100, verbose_name='receiver address')),
                ('recaddresspostal', models.CharField(blank=True, max_length=100, verbose_name='receiver address postal')),
                ('sendoutaddress', models.CharField(blank=True, max_length=100, verbose_name='deliver out address')),
                ('sendoutaddresspostal', models.CharField(blank=True, max_length=100, verbose_name='deliver out address postal')),
                ('mail', models.EmailField(db_index=True, max_length=200, verbose_name='E-mail')),
                ('telephone', models.CharField(blank=True, max_length=100, verbose_name='Telephone')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated_time')),
                ('owner', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='own_user', to='user.User', verbose_name='Who Input')),
            ],
            options={
                'verbose_name': 'user informations',
                'ordering': ('updated_time',),
            },
        ),
    ]
