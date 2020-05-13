# Generated by Django 3.0.3 on 2020-05-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
