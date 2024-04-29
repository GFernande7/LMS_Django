# Generated by Django 5.0.4 on 2024-04-29 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'Новая'), ('In_progress', 'В работе'), ('Completed', 'Завершена')], default='New', max_length=50)),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Очень низкий'), (2, 'Низкий'), (3, 'Средний'), (4, 'Высокий'), (5, 'Очень высокий')], default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug_reports', to='tasks.project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bug_reports', to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Review', 'Рассмотрение'), ('Accepted', 'Принято'), ('Rejected', 'Отклонено')], default='Review', max_length=50)),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Очень низкий'), (2, 'Низкий'), (3, 'Средний'), (4, 'Высокий'), (5, 'Очень высокий')], default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_requests', to='tasks.project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feature_requests', to='tasks.task')),
            ],
        ),
    ]