# Generated by Django 4.1.4 on 2022-12-18 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_remove_savedmedicines_timeof_savedmedicines_intake'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedmedicines',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='medicine.medicinename'),
            preserve_default=False,
        ),
    ]
