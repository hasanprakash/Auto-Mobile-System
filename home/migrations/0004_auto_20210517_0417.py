# Generated by Django 3.1.4 on 2021-05-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210511_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('carcolor', models.CharField(max_length=20)),
                ('detailcolor', models.CharField(max_length=20)),
                ('interiorcolor', models.CharField(max_length=20)),
                ('enginetype', models.CharField(max_length=30)),
                ('rim', models.CharField(max_length=20)),
                ('spoiler', models.CharField(max_length=20)),
                ('storename', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Com',
        ),
        migrations.DeleteModel(
            name='Names',
        ),
    ]