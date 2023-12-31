# Generated by Django 4.2.6 on 2023-10-26 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_product_medida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='medida',
            field=models.ForeignKey(choices=[(1, 'S - 15/25 personas'), (2, 'M - 25/35 personas'), (3, 'L - 35/50 personas'), (4, 'XL - 50/100 personas'), (5, 'XXL - 100/300 personas')], on_delete=django.db.models.deletion.CASCADE, to='myapp.medida', verbose_name='medida'),
        ),
    ]
