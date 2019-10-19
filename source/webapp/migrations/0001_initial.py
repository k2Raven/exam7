# Generated by Django 2.2.6 on 2019-10-19 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=2000, verbose_name='Вопрос')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(max_length=2500, verbose_name='Текст варианта')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='webapp.Poll', verbose_name='Опрос')),
            ],
        ),
    ]
