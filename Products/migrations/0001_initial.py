# Generated by Django 3.0.5 on 2020-06-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('weight', models.IntegerField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
    ]