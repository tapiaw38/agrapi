""" Producer Serizer """

# Rest Framework
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


# Import Models Producer
from producer.models import (
    Pollster,
    Producer, 
    ProducerPerson,
    ProducerHome,
    ProducerVehicle,
    ProducerActivity,
    ActivityWorker,
    Production,
    ProductionService,
    ProductionMachine,
    ProductionProperty,
    ProductionIrrigation,
    ProductionInstallation,
    InstallationBarn,
    InstallationWell,
    ProductionAgricultural,
    AgriculturalSalesChannel,
    AgriculturalAttendance,
    AgriculturalClimatic,
    AgriculturalPests,
    AgriculturalHarvest,
    AgriculturalSalesChannel,
    ProductionLivestock,
    LivestockAnimalFeeding,
    LivestockReproduction,
    LivestockHealth,
    LivestockMarketing,
    LivestockAnimalPens,
    LivestockSalesChannel,
    LivestockBovineCycle,
    LivestockSheepCycle,
    LivestockGoatCycle,
    LivestockPigCycle,
    LivestockLlamaCycle,
    LivestockPoultryCycle,
    LivestockRabbitCycle,
    LivestockBeekeepingCycle,
    LivestockAquacultureCycle,
    ProductionAgroindustrial,
    AgroindustrialTools,
    AgroindustrialFoodProduct,
    AgroindustrialHandmandeProduct,
)

# Serializers Production Agro-industrial
class AgroindustrialHandmandeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroindustrialHandmandeProduct
        fields = (
            'name_product',
            'quantity',
            'price',
        )

class AgroindustrialFoodProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroindustrialFoodProduct
        fields = (
            'id',
            'name_product',
            'validity',
            'origin',
            'quantity',
            'price',
        )

class AgroindustrialToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroindustrialTools
        fields = (
            'id',
            'name_tool',
            'type_tool', 
            'number_tools', 
        )

class ProductionAgroindustrialSerializer(WritableNestedModelSerializer):
    agroindustrial_tools = AgroindustrialToolsSerializer(many=True, allow_null=True)
    agroindustrial_food_product = AgroindustrialFoodProductSerializer(many=True, allow_null=True)
    agroindustrial_handmande_product = AgroindustrialHandmandeProductSerializer(many=True, allow_null=True)
    class Meta:
        model = ProductionAgroindustrial
        fields = (
            'id',
            'description',
            'raw_material',
            'is_mechanized',
            'knowledge',
            'agroindustrial_food_product',
            'agroindustrial_handmande_product',
            'agroindustrial_tools',
        )

# Serializers Production Livestock


class LivestockAquacultureCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockAquacultureCycle
        fields = (
            'id',
            'created',
            'modified',
            'orientation',
            'existence',
        )

class LivestockBeekeepingCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockBeekeepingCycle
        fields = (
            'id',
            'created',
            'modified',
            'renapa',
            'kind_bee',
            'has_bee_hives',
            'type_bee_hives',
            'number_drawers',
            'alsas_drawer',
            'pollination_period',
            'pollinated_flower',
        )

class LivestockRabbitCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockRabbitCycle
        fields = (
            'id',
            'created',
            'modified',
            'orientation',
            'number_breeding_males',
            'number_breeding_females',
            'number_rabbit',
        )

class LivestockPoultryCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockPoultryCycle
        fields = (
            'id',
            'created',
            'modified',
            'is_intensive_poultry',
            'has_hatchery',
            'number_incubators',
            'number_hatching_eggs',
            'chicks_one_two_months',
            'chicks_three_five_months',
            'females_older_six_months',
            'number_broiler_chickens',
            'number_breeder_layers',
            'number_breeding_males',
        )

class LivestockLlamaCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockLlamaCycle
        fields = (
            'id',
            'created',
            'modified',
            'number_tekes',
            'number_tekes_weaned',
            'number_maltones',
            'number_young_females',
            'number_young_males',
            'number_llamas_mothers',
            'number_capons',
        )

class LivestockPigCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockPigCycle
        fields = (
            'id',
            'created',
            'modified',
            'up_three_months',
            'three_eight_months',
            'males_older_eight_months',
            'females_older_eight_months',
            'number_pigs',
            'number_stallions',
        )

class LivestockGoatCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockGoatCycle
        fields = (
            'id',
            'created',
            'modified',
            'goats_under_six_months',
            'goats_six_months_to_first_calving',
            'number_goats',
            'number_capons',
            'number_stallions',
        )

class LivestockSheepCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockSheepCycle
        fields = (
            'id',
            'created',
            'modified',
            'sheep_under_six_months',
            'sheep_older_six_months_to_calving',
            'sheep_older_six_months_one_year',
            'number_sheep',
            'number_capons',
            'number_rams',
        )

class LivestockBovineCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockBovineCycle
        fields = (
            'id',
            'created',
            'modified',
            'calves_under_one_year',
            'heifers_one_to_two_years',
            'heifers_over_two_years',
            'number_cows',
            'steers_one_to_two_years',
            'steers_older_two_years',
            'bulls_one_to_two_years',
            'bulls_older_two_years',
            'number_oxen_torunos',
        )

class LivestockAnimalPensSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockAnimalPens
        fields = (
                'id',
                'orientation',
                'building_material',
                'roof_material',
                'foor_material',
                'surface',
                'num_animals',
                'lat',
                'lng',
        )

class LivestockSalesChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockSalesChannel
        fields = (
          'id',
          'is_collector',
          'is_cooperative',
          'is_exporter',
          'use_baler',
          'use_fair',
          'use_industry',
          'use_fridge',
          'make_direct_sale',
        )

class LivestockMarketingSerializer(WritableNestedModelSerializer):
    livestock_sales_channel = LivestockSalesChannelSerializer(allow_null=True)
    class Meta:
        model = LivestockMarketing
        fields = (
            'id',
            'created',
            'modified',
            'number_slaughtered',
            'slaughter_destination',
            'amount_leather',
            'leather_destination',
            'number_shorn',
            'amount_wool',
            'wool_destination',
            'liters_milk',
            'milk_destination',
            'number_eggs',
            'eggs_destination',
            'honey_yield',
            'honey_destination',
            'amount_feces',
            'feces_destination',
            'livestock_sales_channel',
        )

class LivestockHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockHealth
        fields = (
            'id',
            'type_technical_assistance',
            'vitamin_complex',
            'make_internal_deworming',
            'make_external_deworming',
            'type_antiparasitic',
            'make_vaccination',
            'type_vaccination',
            'type_disease',
            'name_disease',
            'other_practices',
        )

class LivestockReproductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockReproduction
        fields = (
            'id',
            'make_reproductive_management',
            'type_reproductive_management',
            'make_continuous_service',
            'other_practices',
        )
class LivestockAnimalFeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockAnimalFeeding
        fields = (
            'id',
            'feeding',
            'type_feeding',
            'daily_rations',
            'description',
        )

class ProductionLivestockSerializer(WritableNestedModelSerializer):
    livestock_animal_feeding = LivestockAnimalFeddingSerializer(many=True, allow_null=True)
    livestock_reproduction = LivestockReproductionSerializer(allow_null=True)
    livestock_health = LivestockHealthSerializer(allow_null=True)
    livestock_animal_pens = LivestockAnimalPensSerializer(many=True, allow_null=True)
    livestock_marketing = LivestockMarketingSerializer(many=True, allow_null=True)
    livestock_bovine_cycle = LivestockBovineCycleSerializer(many=True, allow_null=True)
    livestock_sheep_cycle = LivestockSheepCycleSerializer(many=True, allow_null=True)
    livestock_goat_cycle = LivestockGoatCycleSerializer(many=True, allow_null=True)
    livestock_pig_cycle = LivestockPigCycleSerializer(many=True, allow_null=True)
    livestock_llama_cycle = LivestockLlamaCycleSerializer(many=True, allow_null=True)
    livestock_poultry_cycle = LivestockPoultryCycleSerializer(many=True, allow_null=True)
    livestock_rabbit_cycle = LivestockRabbitCycleSerializer(many=True, allow_null=True)
    livestock_beekeeping_cycle = LivestockBeekeepingCycleSerializer(many=True, allow_null=True)
    livestock_aquaculture_cycle = LivestockAquacultureCycleSerializer(many=True, allow_null=True)
    class Meta:
        model = ProductionLivestock
        fields = (
            'id',
            'type_activity',
            'surface',
            'destination',
            'make_technical_assistance',
            'problems',
            'suggestion',
            'livestock_animal_feeding',
            'livestock_reproduction',
            'livestock_animal_pens',
            'livestock_health',
            'livestock_marketing',
            'livestock_bovine_cycle',
            'livestock_sheep_cycle',
            'livestock_goat_cycle',
            'livestock_pig_cycle',
            'livestock_llama_cycle',
            'livestock_poultry_cycle',
            'livestock_rabbit_cycle',
            'livestock_beekeeping_cycle',
            'livestock_aquaculture_cycle',
        )

# Serializers Production Agricultural
class AgriculturalSalesChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalSalesChannel
        fields = (
          'id',
          'is_collector',
          'is_cooperative',
          'is_exporter',
          'use_baler',
          'use_fair',
          'use_industry',
          'use_fridge',
          'make_direct_sale',
        )

class AgriculturalHarvestSerializer(WritableNestedModelSerializer):
    agricultural_sales_channel = AgriculturalSalesChannelSerializer(allow_null=True)
    class Meta:
        model = AgriculturalHarvest
        fields = (
            'id',
            'created',
            'modified',
            'harvest_surface',
            'tons_production',
            'harvest_time',
            'agricultural_sales_channel',
        )

class AgriculturalPestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalPests
        fields = (
            'id',
            'type_pests',
            'pests_description',
            'make_pests_control',
            'type_pests_control',
            'make_pesticide',
            'type_pesticide',
            'other_practices',
        )

class AgriculturalClimaticSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalClimatic
        fields = (
            'id',
            'factor',
            'risk',
            'description',
        )

class AgriculturalAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalAttendance
        fields = (
            'id',
            'use_fertilizers',
            'use_food_organic',
            'use_pheromones',
            'use_hail_mesh',
            'make_frost_control',
            'other_practices',
            )

class ProductionAgriculturalSerializer(WritableNestedModelSerializer):
    agricultural_attendance = AgriculturalAttendanceSerializer(allow_null=True)
    agricultural_climatic =  AgriculturalClimaticSerializer(allow_null=True, many=True)
    agricultural_pests =  AgriculturalPestSerializer(allow_null=True, many=True)
    agricultural_harvest = AgriculturalHarvestSerializer(allow_null=True, many=True)
    class Meta:
        model = ProductionAgricultural
        fields = (
            'id',
            'activity_name',
            'variety',
            'surface',
            'destination',
            'sowing',
            'type_sowing',
            'age',
            'perimeter_closure',
            'suggestion',
            'agricultural_attendance',
            'agricultural_climatic',
            'agricultural_pests',
            'agricultural_harvest',
        )

# Serializer related Production
class InstallationBarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallationBarn
        fields = (
            'id',
            'surface',
            'lat',
            'lng',
        )

class InstallationWellSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallationWell
        fields = (
            'id',
            'is_active',
            'lat',
            'lng',
        )

class ProductionInstallationSerializer(WritableNestedModelSerializer):
    installation_barn = InstallationBarnSerializer(many=True, allow_null=True)
    installation_well = InstallationWellSerializer(many=True, allow_null=True)
    class Meta:
        model = ProductionInstallation
        fields = (
            'id',
            'has_windmills',
            'has_australian_tanks',
            'has_dams',
            'has_truck_scale',
            'has_fire_break',
            'has_minced_steel',
            'has_pools',
            "installation_barn",
            "installation_well",
        )
class ProductionIrrigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionIrrigation
        fields = (
            'id',
            'type_irrigation',
            'pressurized_irrigation',
            'surface_irrigation',
            'take_section',
            'watering_hours',
            'channel_conditions',
            'right',
            'shifts',  
        ) 

class ProductionPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionProperty
        fields = (
            'id',
            'land_tenure',
            'has_land_title',
            'cadastre_registration',
            'starting_number',
        )

class ProductionMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionMachine
        fields = (
	        'id',
            'destination',
            'name_machine',
            'type_maquinary',
            'model',
            'state_machine',
            'age',
            'observation',
        )

class ProductionServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionService
        fields = (
            'id',
            'has_service_aqua',
            'type_service_aqua',
            'has_service_energy',
            'type_service_energy',
            'has_rural_energy',
            'has_generator',
            'has_hydraulic_generator',
            'has_solar_panels',
        )

class ProductionSerializer(WritableNestedModelSerializer):
    production_property = ProductionPropertySerializer(allow_null=True)
    production_service = ProductionServiceSerializer(allow_null=True)
    production_installation = ProductionInstallationSerializer(allow_null=True)
    production_machine = ProductionMachineSerializer(many=True, allow_null=True)
    production_irrigation = ProductionIrrigationSerializer(allow_null=True)
    production_agricultural = ProductionAgriculturalSerializer(many=True, allow_null=True)
    production_livestock = ProductionLivestockSerializer(many=True, allow_null=True)
    production_agroindustrial = ProductionAgroindustrialSerializer(many=True, allow_null=True)
    class Meta:
        model = Production
        fields = (
            'id',
            'is_resident', 
            'district',
            'surface',
            'road_state',
            'lat',
            'lng',
            'has_renspa',
            'has_renaf',
            'production_property',
            'production_service',
            'production_installation',
            'production_machine',
            'production_irrigation',
            'production_agricultural',
            'production_livestock',
            'production_agroindustrial',
        )

# Serializers related at Producer
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityWorker
        fields = (
            'id',
            'is_formal_worker',
            'type_person',
            'is_resident',
            'gender',
            'receive_remuneration',
            'work_position',
            'type_job',
        )

class ActivitySerializer(WritableNestedModelSerializer):
    activity_worker = WorkerSerializer(many=True)
    class Meta:
        model = ProducerActivity
        fields = (
            'id',
            'works_under_dependency',
            'is_monotributista',
            'category',
            'use_external_labor',
            'activity_worker',
        )

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerVehicle
        fields = (
            'id',
            'name_vehicle',
            'use_trailer',
            'type_trailer',
            'use_semitrailer',
        )

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerPerson
        fields = (
            'id',
            'family_relation',
            'first_name',
            'last_name',
            'age',
            'has_primary_studies',
            'has_secondary_studies',
            'has_tertiary_studies',
            'has_university_studies',
            'perform_work_activity',
            'description',
        )

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerHome
        fields = (
            'id',
            'district',
            'address',
            'type_recidence',
            'state_recidence',
        )

class ProducerSerializer(WritableNestedModelSerializer):
    producer_home = HomeSerializer(allow_null=True)
    producer_activity = ActivitySerializer(allow_null=True)
    producer_person = PersonSerializer(many=True, allow_null=True)
    producer_vehicle = VehicleSerializer(many=True, allow_null=True)
    # Production
    production = ProductionSerializer(many=True, allow_null=True)


    class Meta:
        model = Producer
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_birth',
            'document',
            'gender',
            'phone_number',
            'producer_home',
            'producer_person',
            'producer_vehicle',
            'producer_activity',
            'production',
        )

class PollsterSerializer(WritableNestedModelSerializer):
    producer = ProducerSerializer(allow_null=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = Pollster
        fields = (
            'id',
            'user',
            'created',
            'modified',
            'producer',
        )
        read_only_fields = [
            'user',
            'created',
        ]


    def create(self,validated_data):
            """ Method create relations serializer 
            of producers & production. """

            # Add user & profile at pollster
            user =  self.context['request'].user
            profile = user.profile
            profile.polls += 1
            profile.save()

            # Create relation of serializers
            producer_data = validated_data.pop('producer')

            pollster = Pollster.objects.create(
                user=user,
                profile=profile
            )
            # Remove data from list 

            # Producer
            home_data = producer_data.pop('producer_home')
            person_data = producer_data.pop('producer_person')
            vehicle_data = producer_data.pop('producer_vehicle')
            activity_data = producer_data.pop('producer_activity')

            # Sub data Producer
            worker_data = activity_data.pop('activity_worker')
            
            # Production
            production_data = producer_data.pop('production')

            # Created objects
            producer = Producer.objects.create(pollster=pollster, **producer_data)
            
            # Sub created objects producer
            activity =  ProducerActivity.objects.create(producer=producer, **activity_data)

        
            # Relation OneToOne
            ProducerHome.objects.create(producer=producer, **home_data)

            # Relation Foreinkey
            for person_data in person_data:
                ProducerPerson.objects.create(producer=producer, **person_data)

            for vehicle_data in vehicle_data:
                ProducerVehicle.objects.create(producer=producer, **vehicle_data)

            # Sub relation activity
            for worker_data in worker_data:
                ActivityWorker.objects.create(activity=activity, **worker_data)
            
            # Production
            for production_data in production_data:
                # remove on list production
                production_property_data = production_data.pop('production_property')
                production_service_data = production_data.pop('production_service')
                production_installation_data = production_data.pop('production_installation')
                production_machine_data = production_data.pop('production_machine')
                production_irrigation_data = production_data.pop('production_irrigation')
                production_agricultural_data = production_data.pop('production_agricultural')
                production_livestock_data = production_data.pop('production_livestock')
                production_agroindustrial_data = production_data.pop('production_agroindustrial')
                
                # Create object production
                production = Production.objects.create(producer=producer, **production_data)

                # sub create objects production
                ProductionProperty.objects.create(production=production, **production_property_data)
                ProductionService.objects.create(production=production, **production_service_data)
                ProductionIrrigation.objects.create(production=production, **production_irrigation_data)

                for production_machine_data in production_machine_data:
                    ProductionMachine.objects.create(production=production, **production_machine_data)
                
                # sub create installations

                installation_barn_data = production_installation_data.pop('installation_barn')
                installation_well_data = production_installation_data.pop('installation_well')

                installation = ProductionInstallation.objects.create(production=production, **production_installation_data)

                for installation_barn_data in installation_barn_data:
                    InstallationBarn.objects.create(installation=installation, **installation_barn_data)
                for installation_well_data in installation_well_data:
                    InstallationWell.objects.create(installation=installation, **installation_well_data)
                
                # Production Agricultural
                for production_agricultural_data in production_agricultural_data:
                    agricultural_attendance_data = production_agricultural_data.pop('agricultural_attendance')
                    agricultural_climatic_data = production_agricultural_data.pop('agricultural_climatic')
                    agricultural_pests_data = production_agricultural_data.pop('agricultural_pests')
                    agricultural_harvest_data = production_agricultural_data.pop('agricultural_harvest')

                    production_agricultural = ProductionAgricultural.objects.create(production=production, **production_agricultural_data)

                    AgriculturalAttendance.objects.create(production_agricultural=production_agricultural, **agricultural_attendance_data)
                    for agricultural_climatic_data in agricultural_climatic_data:
                        AgriculturalClimatic.objects.create(production_agricultural=production_agricultural, **agricultural_climatic_data)
                    for agricultural_pests_data in agricultural_pests_data:
                        AgriculturalPests.objects.create(production_agricultural=production_agricultural, **agricultural_pests_data)
                    
                    for agricultural_harvest_data in agricultural_harvest_data:
                        agricultural_sales_channel_data = agricultural_harvest_data.pop('agricultural_sales_channel')
                        agricultural_harvest = AgriculturalHarvest.objects.create(production_agricultural=production_agricultural, **agricultural_harvest_data)
                        AgriculturalSalesChannel.objects.create(agricultural_harvest=agricultural_harvest, **agricultural_sales_channel_data)
            
                # Production Livestock
                for production_livestock_data in production_livestock_data:
                    livestock_animal_feeding_data = production_livestock_data.pop('livestock_animal_feeding')
                    livestock_reproduction_data = production_livestock_data.pop('livestock_reproduction')
                    livestock_animal_pens_data = production_livestock_data.pop('livestock_animal_pens')
                    livestock_health_data = production_livestock_data.pop('livestock_health')
                    livestock_marketing_data = production_livestock_data.pop('livestock_marketing')
                    livestock_bovine_cycle_data = production_livestock_data.pop('livestock_bovine_cycle')
                    livestock_sheep_cycle_data = production_livestock_data.pop('livestock_sheep_cycle')
                    livestock_goat_cycle_data = production_livestock_data.pop('livestock_goat_cycle')
                    livestock_pig_cycle_data = production_livestock_data.pop('livestock_pig_cycle')
                    livestock_llama_cycle_data = production_livestock_data.pop('livestock_llama_cycle')
                    livestock_poultry_cycle_data = production_livestock_data.pop('livestock_poultry_cycle')
                    livestock_rabbit_cycle_data = production_livestock_data.pop('livestock_rabbit_cycle')
                    livestock_beekeeping_cycle_data = production_livestock_data.pop('livestock_beekeeping_cycle')
                    livestock_aquaculture_cycle_data = production_livestock_data.pop('livestock_aquaculture_cycle')

                    production_livestock = ProductionLivestock.objects.create(production=production, **production_livestock_data)
                    
                    for livestock_animal_feeding_data in livestock_animal_feeding_data:
                        LivestockAnimalFeeding.objects.create(production_livestock=production_livestock, **livestock_animal_feeding_data)
                    LivestockReproduction.objects.create(production_livestock=production_livestock, **livestock_reproduction_data)

                    LivestockHealth.objects.create(production_livestock=production_livestock, **livestock_health_data)
                    
                    for livestock_marketing_data in livestock_marketing_data:
                        livestock_sales_channel_data = livestock_marketing_data.pop('livestock_sales_channel')
                        livestock_marketing = LivestockMarketing.objects.create(production_livestock=production_livestock, **livestock_marketing_data)
                        LivestockSalesChannel.objects.create(livestock_marketing=livestock_marketing, **livestock_sales_channel_data)

                    for livestock_bovine_cycle_data in livestock_bovine_cycle_data:
                        LivestockBovineCycle.objects.create(production_livestock=production_livestock, **livestock_bovine_cycle_data)
                    for livestock_sheep_cycle_data in livestock_sheep_cycle_data:
                        LivestockSheepCycle.objects.create(production_livestock=production_livestock, **livestock_sheep_cycle_data)
                    for livestock_goat_cycle_data in livestock_goat_cycle_data:
                        LivestockGoatCycle.objects.create(production_livestock=production_livestock, **livestock_goat_cycle_data)
                    for livestock_pig_cycle_data in livestock_pig_cycle_data:
                        LivestockPigCycle.objects.create(production_livestock=production_livestock, **livestock_pig_cycle_data)
                    for livestock_llama_cycle_data in livestock_llama_cycle_data:
                        LivestockLlamaCycle.objects.create(production_livestock=production_livestock, **livestock_llama_cycle_data)
                    for livestock_poultry_cycle_data in livestock_poultry_cycle_data:
                        LivestockPoultryCycle.objects.create(production_livestock=production_livestock, **livestock_poultry_cycle_data)
                    for livestock_rabbit_cycle_data in livestock_rabbit_cycle_data:
                        LivestockRabbitCycle.objects.create(production_livestock=production_livestock, **livestock_rabbit_cycle_data)
                    for livestock_beekeeping_cycle_data in livestock_beekeeping_cycle_data:
                        LivestockBeekeepingCycle.objects.create(production_livestock=production_livestock, **livestock_beekeeping_cycle_data)
                    for livestock_aquaculture_cycle_data in livestock_aquaculture_cycle_data:
                        LivestockAquacultureCycle.objects.create(production_livestock=production_livestock, **livestock_aquaculture_cycle_data)
                    for livestock_animal_pens_data in livestock_animal_pens_data:
                        LivestockAnimalPens.objects.create(production_livestock=production_livestock, **livestock_animal_pens_data)

                for production_agroindustrial_data in production_agroindustrial_data:
                    agroindustrial_tools_data = production_agroindustrial_data.pop('agroindustrial_tools')
                    agroindustrial_food_product_data = production_agroindustrial_data.pop('agroindustrial_food_product')
                    agroindustrial_handmande_product_data = production_agroindustrial_data.pop('agroindustrial_handmande_product')

                    production_agroindustrial = ProductionAgroindustrial.objects.create(production=production, **production_agroindustrial_data)

                    for agroindustrial_tools_data in agroindustrial_tools_data:
                        AgroindustrialTools.objects.create(production_agroindustrial=production_agroindustrial, **agroindustrial_tools_data)

                    for agroindustrial_food_product_data in agroindustrial_food_product_data:
                        AgroindustrialFoodProduct.objects.create(production_agroindustrial=production_agroindustrial, **agroindustrial_food_product_data)

                    for agroindustrial_handmande_product_data in agroindustrial_handmande_product_data:
                        AgroindustrialHandmandeProduct.objects.create(production_agroindustrial=production_agroindustrial, **agroindustrial_handmande_product_data)

            return pollster
