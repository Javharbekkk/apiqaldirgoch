# Generated by Django 5.1.2 on 2024-10-24 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_question_basisquestvariant_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basisquest',
            name='intellect_quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BasisVariants', to='main.basisquestvariant'),
        ),
        migrations.AlterField(
            model_name='intelectquest',
            name='intellect_quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IntelektVariants', to='main.intelectquestvariant'),
        ),
    ]
