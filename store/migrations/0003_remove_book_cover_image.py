from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_alter_book_cover_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="cover_image",
        ),
    ]
