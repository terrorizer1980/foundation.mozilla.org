# Generated by Django 2.2.17 on 2021-03-23 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0008_auto_20210126_1943'),
        ('wagtailpages', '0051_auto_20210317_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.DeleteModel(
            name='BuyersGuideProductCategory',
        ),
    ]
