# Generated by Django 3.0.3 on 2020-04-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialogs', '0002_message_is_readed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_image',
            field=models.ImageField(blank=True, upload_to='images/messages/', verbose_name='Изображение'),
        ),
    ]
