# Generated by Django 2.1 on 2019-10-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MqttAcls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('pw', models.CharField(max_length=200)),
                ('superuser', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
