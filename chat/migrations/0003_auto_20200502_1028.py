# Generated by Django 3.0 on 2020-05-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200502_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_contact_friends_+', to='chat.Contact'),
        ),
    ]
