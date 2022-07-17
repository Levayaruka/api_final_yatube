# Generated by Django 2.2.16 on 2022-07-16 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_group_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_group', to='posts.Group'),
        ),
    ]