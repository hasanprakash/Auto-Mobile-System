# Generated by Django 3.1.4 on 2021-05-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_details_ordercancelled'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCancelledFeedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('feedback', models.TextField(max_length=1513)),
            ],
        ),
    ]
