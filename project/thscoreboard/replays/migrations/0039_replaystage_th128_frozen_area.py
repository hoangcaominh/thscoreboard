# Generated by Django 4.2.1 on 2023-05-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("replays", "0038_merge_20230524_1817"),
    ]

    operations = [
        migrations.AddField(
            model_name="replaystage",
            name="th128_frozen_area",
            field=models.FloatField(blank=True, null=True),
        ),
    ]