# Generated by Django 3.2.5 on 2021-08-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog!', max_length=255),
        ),
    ]
