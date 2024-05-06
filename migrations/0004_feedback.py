# Generated by Django 4.0 on 2023-11-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAVApp', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
