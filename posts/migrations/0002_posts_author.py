# Generated by Django 5.0.6 on 2024-07-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
