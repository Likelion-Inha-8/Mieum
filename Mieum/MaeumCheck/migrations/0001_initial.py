# Generated by Django 3.0.8 on 2020-09-20 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('meeting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MaeumCheck.Meeting')),
                ('address', models.CharField(max_length=100)),
                ('maxPeople', models.IntegerField()),
                ('currentPeople', models.IntegerField()),
                ('congestion', models.IntegerField()),
            ],
            bases=('MaeumCheck.meeting',),
        ),
        migrations.CreateModel(
            name='Meeting_Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_at', models.DateTimeField(auto_now_add=True)),
                ('visiter', models.CharField(max_length=50)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MaeumCheck.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Place_Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_at', models.DateTimeField(auto_now_add=True)),
                ('visiter', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MaeumCheck.Place')),
            ],
        ),
    ]