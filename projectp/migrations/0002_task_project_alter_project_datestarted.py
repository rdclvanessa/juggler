# Generated by Django 4.2.5 on 2023-09-11 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='projectA', on_delete=django.db.models.deletion.CASCADE, to='projectp.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='dateStarted',
            field=models.DateField(default=(2023, 11, 11), verbose_name='Date the project was started.'),
            preserve_default=False,
        ),
    ]