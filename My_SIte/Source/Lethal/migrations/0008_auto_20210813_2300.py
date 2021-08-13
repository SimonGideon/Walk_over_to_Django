# Generated by Django 3.2.4 on 2021-08-13 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lethal', '0007_auto_20210813_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='Lethal.Membership', to='Lethal.Persona'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lethal.persona'),
        ),
    ]
