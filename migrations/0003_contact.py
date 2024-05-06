# Generated by Django 4.0 on 2023-11-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAVApp', '0002_video_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('Issue', models.TextField(max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
