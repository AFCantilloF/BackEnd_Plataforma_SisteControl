# Generated by Django 3.0.6 on 2020-05-21 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200520_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='id_nivel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Niveles'),
        ),
    ]