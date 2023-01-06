# Generated by Django 4.1.5 on 2023-01-04 01:58

import django.core.validators
from django.db import migrations, models
import djongo.storage


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_cours_pdf_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='pdf_cours',
            field=models.FileField(blank=True, storage=djongo.storage.GridFSStorage(base_url='/myfiles/', collection='myfiles'), upload_to='teststandards1', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]