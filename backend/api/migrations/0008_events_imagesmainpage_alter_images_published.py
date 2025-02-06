# Generated by Django 5.1.5 on 2025-02-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_images_options_remove_images_image_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Events",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=250)),
                ("description", models.TextField(blank=True)),
                ("published", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Событие",
                "verbose_name_plural": "События",
                "ordering": ["published"],
            },
        ),
        migrations.CreateModel(
            name="ImagesMainPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(default=None, upload_to="images/main/")),
                ("published", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Изображение на главной странице",
                "verbose_name_plural": "Изображения на главной странице",
                "ordering": ["-published"],
            },
        ),
        migrations.AlterField(
            model_name="images",
            name="published",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
