# Generated by Django 4.2.11 on 2024-03-14 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default-blog.jpg', upload_to='blog_pics'),
        ),
    ]
