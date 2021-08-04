# Generated by Django 3.2.6 on 2021-08-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crystal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('weight', models.FloatField()),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('origin', models.TextField()),
                ('title', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'crystals',
            },
        ),
    ]
