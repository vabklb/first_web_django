# Generated by Django 3.2.5 on 2021-07-20 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsss', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cateegorias',
            new_name='categorias',
        ),
    ]