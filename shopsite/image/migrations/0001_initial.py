# Generated by Django 2.2.6 on 2019-10-23 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0001_initial'),
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=40, verbose_name='slug')),
                ('image', models.ImageField(upload_to='image/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comment_img', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_images', to='comment.Comment', verbose_name='belongstoComment')),
                ('product_img', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='product.Product', verbose_name='belongstoProduct')),
                ('user_img', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_images', to='user.User', verbose_name='belongstoUser')),
            ],
            options={
                'verbose_name': 'image',
                'ordering': ('created',),
            },
        ),
    ]
