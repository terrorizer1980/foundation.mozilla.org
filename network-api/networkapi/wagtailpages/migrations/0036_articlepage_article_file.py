# Generated by Django 2.2.17 on 2021-02-17 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('wagtailpages', '0035_auto_20210209_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='article_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]