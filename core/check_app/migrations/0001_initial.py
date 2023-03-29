# Generated by Django 4.1.7 on 2023-03-27 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('api_key', models.CharField(max_length=100)),
                ('check_type', models.CharField(max_length=100)),
                ('point_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=130)),
                ('order', models.JSONField()),
                ('status', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to='pdf')),
                ('printer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check_app.printer')),
            ],
        ),
    ]