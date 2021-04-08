# Generated by Django 3.0.3 on 2021-04-08 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorname', models.CharField(max_length=10)),
                ('colorurl', models.ImageField(upload_to='color/')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=100)),
                ('gdesc', models.CharField(max_length=100)),
                ('oldprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsDetailName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Color')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Size')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdurl', models.ImageField(upload_to='')),
                ('gdname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsDetailName')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
        ),
    ]