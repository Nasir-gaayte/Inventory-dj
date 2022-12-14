# Generated by Django 4.1.2 on 2022-10-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost_product', models.DecimalField(decimal_places=2, max_digits=20)),
                ('qty_in_stock', models.IntegerField()),
                ('qty_sold', models.IntegerField()),
                ('sales', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stack_date', models.DateField(auto_now_add=True)),
                ('last_sales_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
