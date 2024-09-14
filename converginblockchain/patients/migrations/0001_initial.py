# Generated by Django 2.1.5 on 2019-06-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patientsymptomsanalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patintid', models.CharField(max_length=10)),
                ('patinetname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=60)),
                ('patinetallsymptoms', models.CharField(max_length=600)),
                ('diseasname', models.CharField(max_length=250)),
                ('descriptions', models.CharField(max_length=600)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
