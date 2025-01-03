# Generated by Django 5.1.2 on 2024-10-26 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.TextField()),
                ('score', models.IntegerField()),
                ('operation', models.TextField()),
                ('gamelength', models.TextField()),
                ('maxnum', models.TextField()),
                ('game', models.TextField(choices=[('MATH FACTS', 'Math Facts'), ('ANAGRAM HUNT', 'Anagram Hunt')], default='MATH FACTS')),
            ],
        ),
    ]
