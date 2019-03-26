# Generated by Django 2.1.7 on 2019-03-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190324_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dweeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('pswd', models.CharField(max_length=16)),
                ('fullname', models.CharField(blank=True, max_length=32)),
                ('country', models.CharField(blank=True, max_length=32)),
                ('crDate', models.DateTimeField(auto_now_add=True)),
                ('crBy', models.IntegerField(default=0)),
                ('lmodDate', models.DateTimeField(auto_now=True)),
                ('lmodBy', models.IntegerField(default=0)),
                ('isActive', models.IntegerField(default=1)),
            ],
        ),
    ]
