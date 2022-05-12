# Generated by Django 3.2.8 on 2022-03-06 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_learning'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='learning',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='learning',
            name='bookmark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.bookmark'),
        ),
    ]
