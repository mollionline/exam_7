# Generated by Django 4.0.2 on 2022-02-12 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Автор 1', max_length=50)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('death_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(default='Описание 1', max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.author', verbose_name='Автор'),
        ),
    ]
