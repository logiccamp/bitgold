# Generated by Django 3.2.4 on 2021-07-07 13:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=11)),
                ('amountreturn', models.DecimalField(decimal_places=2, max_digits=11)),
                ('btcdeposit', models.FloatField(max_length=20)),
                ('btcreturn', models.FloatField(max_length=20)),
                ('plan', models.ManyToManyField(related_name='investments', to='main.Plan')),
                ('user', models.ManyToManyField(related_name='investments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
