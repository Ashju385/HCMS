# Generated by Django 4.1.2 on 2022-10-06 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(choices=[('Swimming Pool', 'Swimming Pool'), ('Picnic Spot', 'Picnic Spot'), ('Community Hall', 'Community Hall')], max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True)),
                ('date_ordered', models.DateTimeField(auto_now=True, null=True)),
                ('date_finished', models.DateTimeField(auto_now_add=True, null=True)),
                ('member_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.member')),
            ],
        ),
    ]