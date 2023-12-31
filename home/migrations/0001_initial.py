# Generated by Django 4.2.4 on 2023-08-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='projectuploads')),
                ('info', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('level 1', 'level 1'), ('level 2', 'level 2'), ('level 3', 'level 3')], max_length=50)),
            ],
        ),
    ]
