# Generated by Django 4.0 on 2023-05-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lati', '0002_facturac_user_facturav_user_alter_producto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturac',
            name='fecha',
            field=models.DateField(max_length=20),
        ),
    ]
