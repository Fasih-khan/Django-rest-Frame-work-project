# Generated by Django 4.0.2 on 2024-01-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_diabaties_age_alter_diabaties_bloodpressure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabaties',
            name='Age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='diabaties',
            name='BloodPressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='diabaties',
            name='Glucose',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='diabaties',
            name='Insulin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='diabaties',
            name='Outcome',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='diabaties',
            name='Pregnancies',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='diabaties',
            name='SkinThickness',
            field=models.IntegerField(),
        ),
    ]
