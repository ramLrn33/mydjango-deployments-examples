# Generated by Django 3.0.3 on 2020-06-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=264)),
                ('LastName', models.CharField(max_length=264)),
                ('Email', models.EmailField(max_length=264)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
