# Generated by Django 3.2.3 on 2021-05-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
