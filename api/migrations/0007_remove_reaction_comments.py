# Generated by Django 5.0.7 on 2024-07-20 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_reaction_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reaction',
            name='comments',
        ),
    ]