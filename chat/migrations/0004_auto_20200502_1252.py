# Generated by Django 3.0 on 2020-05-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20200502_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='participants',
            field=models.ManyToManyField(related_name='chats', to='chat.Contact'),
        ),
    ]