# Generated by Django 3.0.3 on 2020-05-10 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('imbd_id', models.CharField(max_length=200)),
                ('movie_title', models.CharField(max_length=500)),
                ('genero', models.CharField(max_length=200)),
                ('original_language', models.CharField(max_length=200)),
                ('overview', models.CharField(max_length=50000)),
                ('poster_path', models.CharField(max_length=5000)),
                ('release_date', models.CharField(max_length=200)),
                ('budget', models.CharField(max_length=200)),
                ('revenue', models.CharField(max_length=200)),
                ('runtime', models.CharField(max_length=200)),
                ('vote_average', models.CharField(max_length=200)),
                ('tagline', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserFavoriteMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorited_movie_id', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
