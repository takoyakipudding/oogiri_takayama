# Generated by Django 4.2.6 on 2024-01-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agendapp", "0006_alter_information_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="category",
            field=models.CharField(choices=[("写真", 1), ("お題", 2)], max_length=100),
        ),
    ]
