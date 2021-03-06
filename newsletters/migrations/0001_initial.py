# Generated by Django 3.2 on 2022-02-01 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('target', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_news', to=settings.AUTH_USER_MODEL)),
                ('subscribers', models.ManyToManyField(related_name='suscriber_news', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='newsletter', to='tags.Tag')),
                ('voters', models.ManyToManyField(related_name='voters_news', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
