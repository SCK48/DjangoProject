# Generated by Django 3.0.3 on 2020-05-12 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20200512_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
