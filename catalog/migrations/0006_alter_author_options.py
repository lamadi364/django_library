# Generated by Django 5.0.2 on 2024-03-02 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_change_author', 'can change author detail'), ('can_delete_author', 'can detele author with no books'))},
        ),
    ]