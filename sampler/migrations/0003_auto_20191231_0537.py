# Generated by Django 2.0.3 on 2019-12-31 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampler', '0002_slice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='file',
            new_name='audio',
        ),
        migrations.RenameField(
            model_name='slice',
            old_name='file',
            new_name='audio',
        ),
    ]
