# Generated by Django 4.2.4 on 2023-11-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htp_test', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htp',
            name='created_date',
            field=models.DateField(default='2023-11-21'),
        ),
        migrations.AlterField(
            model_name='image_tree',
            name='image',
            field=models.ImageField(upload_to='img_tree/tree.jpg'),
        ),
    ]