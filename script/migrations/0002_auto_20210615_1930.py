# Generated by Django 3.2.4 on 2021-06-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hindi', models.CharField(max_length=64)),
                ('roman', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='words',
            field=models.ManyToManyField(related_name='words', to='script.Word'),
        ),
    ]