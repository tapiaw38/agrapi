# Generated by Django 2.2.12 on 2021-01-07 23:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_formal_worker', models.BooleanField()),
                ('type_person', models.CharField(max_length=50)),
                ('is_resident', models.BooleanField()),
                ('gender', models.CharField(max_length=10)),
                ('receive_remuneration', models.BooleanField()),
                ('work_position', models.CharField(max_length=50)),
                ('type_job', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AgriculturalAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_fertilizers', models.BooleanField()),
                ('use_food_organic', models.BooleanField()),
                ('use_pheromones', models.BooleanField()),
                ('use_hail_mesh', models.BooleanField()),
                ('make_frost_control', models.BooleanField()),
                ('other_practices', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgriculturalClimatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor', models.CharField(max_length=100)),
                ('risk', models.CharField(max_length=50)),
                ('damange_level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AgriculturalHarvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_surface', models.FloatField()),
                ('tons_production', models.FloatField()),
                ('has_curtains_insulated', models.BooleanField()),
                ('plant_length_curtains', models.FloatField(default=0)),
                ('plant_species_curtains', models.CharField(blank=True, max_length=100, null=True)),
                ('harvest_time', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AgriculturalPests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pests', models.CharField(max_length=20)),
                ('pests_description', models.CharField(blank=True, max_length=100, null=True)),
                ('make_pests_control', models.BooleanField()),
                ('make_pesticide', models.BooleanField()),
                ('type_pesticide', models.CharField(blank=True, max_length=40, null=True)),
                ('other_practices', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgriculturalSalesChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_collector', models.BooleanField()),
                ('is_cooperative', models.BooleanField()),
                ('is_exporter', models.BooleanField()),
                ('use_baler', models.BooleanField()),
                ('use_fair', models.BooleanField()),
                ('use_industry', models.BooleanField()),
                ('use_fridge', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AgroindustrialFoodProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=30)),
                ('validity', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AgroindustrialHandmandeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AgroindustrialTools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tool', models.CharField(max_length=50)),
                ('type_tool', models.CharField(max_length=30)),
                ('number_tools', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstallationBarn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface', models.FloatField(default=0)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='InstallationWell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LivestockAnimalFeeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeding', models.CharField(max_length=30)),
                ('type_feeding', models.CharField(max_length=30)),
                ('daily_rations', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LivestockAnimalPens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(max_length=20)),
                ('building_material', models.CharField(max_length=50)),
                ('roof_material', models.CharField(max_length=30)),
                ('foor_material', models.CharField(max_length=30)),
                ('surface', models.FloatField()),
                ('num_animals', models.PositiveIntegerField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LivestockAquacultureCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(blank=True, max_length=30, null=True)),
                ('existence', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockBeekeepingCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_bee', models.CharField(blank=True, max_length=20, null=True)),
                ('has_bee_hives', models.BooleanField()),
                ('type_bee_hives', models.CharField(blank=True, max_length=20, null=True)),
                ('number_drawers', models.PositiveIntegerField(default=0)),
                ('alsas_drawer', models.PositiveIntegerField(default=0)),
                ('type_drawer', models.CharField(blank=True, max_length=20, null=True)),
                ('honey_stones', models.PositiveIntegerField(default=0)),
                ('pollination_period', models.CharField(blank=True, max_length=50, null=True)),
                ('pollinated_flower', models.CharField(blank=True, max_length=50, null=True)),
                ('has_renapa', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='LivestockBovineCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calves_under_one_year', models.PositiveIntegerField(default=0)),
                ('heifers_one_to_two_years', models.PositiveIntegerField(default=0)),
                ('heifers_over_two_years', models.PositiveIntegerField(default=0)),
                ('number_cows', models.PositiveIntegerField(default=0)),
                ('steers_one_to_two_years', models.PositiveIntegerField(default=0)),
                ('steers_older_two_years', models.PositiveIntegerField(default=0)),
                ('bulls_one_to_two_years', models.PositiveIntegerField(default=0)),
                ('bulls_older_two_years', models.PositiveIntegerField(default=0)),
                ('number_oxen_torunos', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockGoatCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goats_under_six_months', models.PositiveIntegerField(default=0)),
                ('goats_six_months_to_first_calving', models.PositiveIntegerField(default=0)),
                ('number_goats', models.PositiveIntegerField(default=0)),
                ('number_capons', models.PositiveIntegerField(default=0)),
                ('number_stallions', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockHealth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_technical_assistance', models.CharField(max_length=20)),
                ('vitamin_complex', models.CharField(blank=True, max_length=30, null=True)),
                ('make_internal_deworming', models.BooleanField()),
                ('make_external_deworming', models.BooleanField()),
                ('type_antiparasitic', models.CharField(blank=True, max_length=30, null=True)),
                ('make_vaccination', models.BooleanField()),
                ('type_vaccination', models.CharField(blank=True, max_length=30, null=True)),
                ('type_disease', models.CharField(blank=True, max_length=20, null=True)),
                ('other_practices', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockLlamaCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_chitas_teques', models.PositiveIntegerField(default=0)),
                ('number_maltones', models.PositiveIntegerField(default=0)),
                ('number_janachos', models.PositiveIntegerField(default=0)),
                ('number_llamas_mothers', models.PositiveIntegerField(default=0)),
                ('number_capons', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockMarketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_slaughtered', models.PositiveIntegerField(default=0)),
                ('number_shorn', models.PositiveIntegerField(default=0)),
                ('amount_wool_hair', models.PositiveIntegerField(default=0)),
                ('amount_leather', models.PositiveIntegerField(default=0)),
                ('liters_milk', models.PositiveIntegerField(default=0)),
                ('milk_destination', models.CharField(blank=True, max_length=100, null=True)),
                ('wool_hair_destination', models.CharField(blank=True, max_length=100, null=True)),
                ('leather_destination', models.CharField(blank=True, max_length=100, null=True)),
                ('slaughter_destination', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockPigCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_two_months', models.PositiveIntegerField(default=0)),
                ('older_two_months', models.PositiveIntegerField(default=0)),
                ('less_four_months', models.PositiveIntegerField(default=0)),
                ('older_four_months', models.PositiveIntegerField(default=0)),
                ('number_pigs', models.PositiveIntegerField(default=0)),
                ('number_stallions', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockPoultryCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_intensive_poultry', models.BooleanField()),
                ('number_broilers_incubated', models.PositiveIntegerField(default=0)),
                ('breeding_males', models.PositiveIntegerField(default=0)),
                ('number_eggs_chickens_babies', models.PositiveIntegerField(default=0)),
                ('number_incubators', models.PositiveIntegerField(default=0)),
                ('number_broilers_fattening', models.PositiveIntegerField(default=0)),
                ('number_breeding_layers', models.PositiveIntegerField(default=0)),
                ('existence', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockRabbitCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(blank=True, max_length=20, null=True)),
                ('number_breeding_males', models.PositiveIntegerField(default=0)),
                ('number_breeding_females', models.PositiveIntegerField(default=0)),
                ('number_rabbit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockReproduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_reproductive_management', models.BooleanField()),
                ('make_continuous_service', models.BooleanField()),
                ('make_corral_service', models.BooleanField()),
                ('make_artificial_insemination', models.BooleanField()),
                ('make_embryo_transplant', models.BooleanField()),
                ('other_practices', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LivestockSalesChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_collector', models.BooleanField()),
                ('is_cooperative', models.BooleanField()),
                ('is_exporter', models.BooleanField()),
                ('use_baler', models.BooleanField()),
                ('use_fair', models.BooleanField()),
                ('use_industry', models.BooleanField()),
                ('use_fridge', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='LivestockSheepCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheep_under_six_months', models.PositiveIntegerField(default=0)),
                ('sheep_older_six_months_to_calving', models.PositiveIntegerField(default=0)),
                ('sheep_older_six_months_one_year', models.PositiveIntegerField(default=0)),
                ('number_sheep', models.PositiveIntegerField(default=0)),
                ('number_capons', models.PositiveIntegerField(default=0)),
                ('number_rams', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pollster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=10)),
                ('document', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='Debes ingresar un número de DNI sin puntos.', regex='\\d{8,8}$')])),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Debes ingresar un número con el siguiente formato: 3837430000. Hasta 10 digitos.', regex='\\d{10,10}$')])),
                ('pollster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='producer', to='producer.Pollster')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_resident', models.BooleanField()),
                ('district', models.CharField(max_length=50)),
                ('surface', models.FloatField()),
                ('road_state', models.CharField(max_length=200)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('has_renspa', models.BooleanField()),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production', to='producer.Producer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_service_aqua', models.BooleanField()),
                ('type_service_aqua', models.CharField(max_length=30)),
                ('has_service_energy', models.BooleanField()),
                ('type_service_energy', models.CharField(max_length=100)),
                ('has_rural_energy', models.BooleanField()),
                ('has_generator', models.BooleanField()),
                ('has_hydraulic_generator', models.BooleanField()),
                ('has_solar_panels', models.BooleanField()),
                ('production', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='production_service', to='producer.Production')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_tenure', models.CharField(max_length=30)),
                ('has_land_title', models.BooleanField()),
                ('cadastre_registration', models.CharField(blank=True, max_length=30, null=True)),
                ('starting_number', models.CharField(blank=True, max_length=30, null=True)),
                ('production', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='production_property', to='producer.Production')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=30)),
                ('name_machine', models.CharField(max_length=100)),
                ('type_maquinary', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('state_machine', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('observation', models.CharField(blank=True, max_length=100, null=True)),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_machine', to='producer.Production')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionLivestock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_activity', models.CharField(max_length=30)),
                ('surface', models.FloatField(default=0)),
                ('destination', models.CharField(max_length=30)),
                ('make_technical_assistance', models.BooleanField()),
                ('problems', models.CharField(blank=True, max_length=200, null=True)),
                ('suggestion', models.CharField(blank=True, max_length=200, null=True)),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_livestock', to='producer.Production')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionIrrigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_irrigation', models.CharField(blank=True, max_length=20, null=True)),
                ('pressurized_irrigation', models.CharField(blank=True, max_length=20, null=True)),
                ('surface_irrigation', models.CharField(blank=True, max_length=20, null=True)),
                ('take_section', models.CharField(blank=True, max_length=20, null=True)),
                ('watering_hours', models.FloatField(default=0)),
                ('channel_conditions', models.CharField(blank=True, max_length=50, null=True)),
                ('right', models.CharField(blank=True, max_length=20, null=True)),
                ('shifts', models.CharField(blank=True, max_length=50, null=True)),
                ('production', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='production_irrigation', to='producer.Production')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_windmills', models.BooleanField()),
                ('has_australian_tanks', models.BooleanField()),
                ('has_dams', models.BooleanField()),
                ('has_truck_scale', models.BooleanField()),
                ('has_fire_break', models.BooleanField()),
                ('has_minced_steel', models.BooleanField()),
                ('has_pools', models.BooleanField()),
                ('production', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='production_installation', to='producer.Production')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionAgroindustrial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('raw_material', models.CharField(max_length=20)),
                ('is_mechanized', models.BooleanField()),
                ('knowledge', models.CharField(max_length=30)),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_agroindustrial', to='producer.Production')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionAgricultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Agricola', max_length=15)),
                ('activity_name', models.CharField(max_length=50)),
                ('surface', models.FloatField()),
                ('destination', models.CharField(max_length=20)),
                ('sowing', models.CharField(max_length=20)),
                ('type_sowing', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('problems', models.CharField(blank=True, max_length=100, null=True)),
                ('suggestion', models.CharField(blank=True, max_length=100, null=True)),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_agricultural', to='producer.Production')),
            ],
        ),
        migrations.CreateModel(
            name='ProducerVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vehicle', models.CharField(max_length=50)),
                ('use_trailer', models.BooleanField()),
                ('type_trailer', models.CharField(blank=True, max_length=50, null=True)),
                ('use_semitrailer', models.BooleanField()),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producer_vehicle', to='producer.Producer')),
            ],
        ),
        migrations.CreateModel(
            name='ProducerPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_relation', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(default=0)),
                ('has_primary_studies', models.BooleanField()),
                ('has_secondary_studies', models.BooleanField()),
                ('has_tertiary_studies', models.BooleanField()),
                ('has_university_studies', models.BooleanField()),
                ('perform_work_activity', models.BooleanField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producer_person', to='producer.Producer')),
            ],
        ),
        migrations.CreateModel(
            name='ProducerHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('address', models.CharField(help_text='Dirección particular', max_length=50)),
                ('type_recidence', models.CharField(help_text='Tipo de recidencia', max_length=50)),
                ('state_recidence', models.CharField(max_length=30)),
                ('producer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='producer_home', to='producer.Producer')),
            ],
        ),
        migrations.CreateModel(
            name='ProducerActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('works_under_dependency', models.BooleanField()),
                ('is_monotributista', models.BooleanField()),
                ('category', models.CharField(blank=True, max_length=2, null=True)),
                ('use_external_labor', models.BooleanField(help_text='Contrata mano de obra externa para s emprendimiento')),
                ('producer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='producer_activity', to='producer.Producer')),
            ],
        ),
    ]
