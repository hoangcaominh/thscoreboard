# Generated by Django 4.1.4 on 2023-02-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("replays", "0023_replaystage_extends_replaystage_th13_trance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="replay",
            name="category",
            field=models.IntegerField(
                choices=[
                    (1, "Regular"),
                    (2, "Tool-Assisted"),
                    (3, "Unusual"),
                    (4, "Private"),
                ]
            ),
        ),
    ]
