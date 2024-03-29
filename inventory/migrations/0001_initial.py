# Generated by Django 2.2.7 on 2019-11-07 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tub',
            fields=[
                ('status', models.CharField(choices=[('TK', 'On Truck'), ('CS', 'Customer Site'), ('DF', 'Docked Full'), ('DE', 'Docked Empty')], default='DE', max_length=2)),
                ('fill', models.CharField(choices=[('ICE_3', '3 Mill'), ('ICE_16', '16 Mill'), ('ICE_BLOCK', 'Ice Block'), ('BAGGED_ICE_3', '3 Mill Bagged'), ('BAGGED_ICE_16', '16 Mill Bagged')], default='ICE_3', max_length=13)),
                ('barcode', models.CharField(max_length=15, unique=True)),
                ('serial_number', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('emp_init', models.CharField(max_length=3)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('status', models.CharField(choices=[('TK', 'On Truck'), ('CS', 'Customer Site'), ('DF', 'Docked Full'), ('DE', 'Docked Empty'), ('RT', 'Retest')], default='DF', max_length=2)),
                ('fill', models.CharField(choices=[('AC', 'Acetylene'), ('AR', 'Argon'), ('BG', 'Beer Gas'), ('CD', 'Carbon Dioxide'), ('GS', 'Guinness Gas'), ('HE', 'Helium'), ('C2', 'Mix C2'), ('C10', 'Mix C10'), ('C25', 'Mix C25'), ('NI', 'Nitrogen'), ('OX', 'Oxygen'), ('ST', 'Stargon'), ('SY', 'Syphon')], max_length=3)),
                ('size', models.CharField(choices=[('T', 'T'), ('K', 'K'), ('S', 'S'), ('D', 'D'), ('Q', 'Q'), ('R', 'R'), ('50', '50'), ('40', '40'), ('20', '20'), ('15', '15'), ('10', '10'), ('5', '5'), ('2.5', '2.5')], default='T', max_length=3)),
                ('barcode', models.CharField(max_length=15, unique=True)),
                ('serial_number', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('emp_init', models.CharField(max_length=3)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.Order')),
            ],
        ),
    ]
