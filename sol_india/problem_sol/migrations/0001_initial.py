# Generated by Django 4.2.7 on 2023-11-07 16:57

import datetime
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
            name='publicPOST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_content', models.TextField(default=None)),
                ('post_image', models.ImageField(default=None, null=True, upload_to='')),
                ('is_question', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 7, 22, 27, 59, 586379, tzinfo=datetime.timezone.utc), null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='publicLIKE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LIKER_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='problem_sol.publicpost')),
            ],
        ),
        migrations.CreateModel(
            name='publicCOMMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default='hello', null=True)),
                ('commenter_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='problem_sol.publicpost')),
            ],
        ),
    ]
