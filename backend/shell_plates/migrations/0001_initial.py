# Generated by Django 3.1.7 on 2021-02-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsequenceFactorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_to_repair', models.CharField(choices=[('No internal entry required, limited repair, no limitation on repair time', 'No internal entry required, limited repair, no limitation on repair time'), ('Internal entry required, limited repair (<3 months)', 'Internal entry required, limited repair (<3 months)'), ('Internal entry required, major repair (3-8 months)', 'Internal entry required, major repair (3-8 months)'), ('Internal entry required, major repair (>8 months)', 'Internal entry required, major repair (>8 months)')], max_length=100, verbose_name='7a: Time to repair')),
                ('cost_of_repair', models.CharField(choices=[('Negligible or less than 5% of capital cost', 'Negligible or less than 5% of capital cost'), ('5-10% of capital cost', '5-10% of capital cost'), ('10-50% of capital cost', '10-50% of capital cost'), ('>50% of capital cost (new tank)', '>50% of capital cost (new tank)')], max_length=100, verbose_name='7b: Cost of repair')),
                ('probable_magnitude_of_product_loss', models.CharField(choices=[('No release of product', 'No release of product'), ('<5% of tank contents', '<5% of tank contents'), ('>5% of tank contents', '>5% of tank contents')], max_length=100, verbose_name='7c: Probable magnitude of product loss')),
                ('likelihood_of_injury_to_personnel', models.CharField(choices=[('No injury or near miss', 'No injury or near miss'), ('Minor injury', 'Minor injury'), ('Lost time injury/Medical treatment', 'Lost time injury/Medical treatment'), ('Serious injury/fatality on site', 'Serious injury/fatality on site')], max_length=100, verbose_name='9a: Likelihood of injury to personnel')),
                ('product_flammability_as_per_MCSP', models.CharField(choices=[('Class III(1) and unclassified product', 'Class III(1) and unclassified product'), ('Class II(1) product', 'Class II(1) product'), ('Class II(2) and III(2) product', 'Class II(2) and III(2) product'), ('Class I product', 'Class I product')], max_length=100, verbose_name='9b: Product flammability as per MCSP')),
                ('product_toxicity', models.CharField(choices=[('Non-toxic substances', 'Non-toxic substances'), ('Toxic substance if in contact with other substances', 'Toxic substance if in contact with other substances'), ('Toxic substance', 'Toxic substance'), ('Extremely toxic substance', 'Extremely toxic substance')], max_length=100, verbose_name='9c: Product toxicity')),
                ('location_of_tank_farm', models.CharField(choices=[('Tank farm within an abandonned area', 'Tank farm within an abandonned area'), ('Flat tank farm', 'Flat tank farm'), ('Flopping tank farm', 'Flopping tank farm'), ('In plant area within populous area', 'In plant area within populous area')], max_length=100, verbose_name='9d: Location of tank farm')),
                ('continued_location_of_tank_farm', models.CharField(choices=[('No public fence near tank farm', 'No public fence near tank farm'), ('Presence of public fence near tank farm', 'Presence of public fence near tank farm')], max_length=100, verbose_name="9d-cont'd: Location of tank farm")),
                ('environmetal_hazard_to_soil_and_water_as_the_potential_to_cause', models.CharField(choices=[('No or negligle environment effect', 'No or negligle environment effect'), ('Environmental nuisance affecting neighbourhood', 'Environmental nuisance affecting neighbourhood'), ('Environmental pollution/Extensive restoration required', 'Environmental pollution/Extensive restoration required'), ('Severe demage/nuisance/pollution over large area', 'Severe demage/nuisance/pollution over large area')], max_length=100, verbose_name='11a: Environmetal hazard to soil and water as the potential to cause')),
                ('vapour_emission', models.CharField(choices=[('No or negligle harmful (toxic) release', 'No or negligle harmful (toxic) release'), ('Small harmful (toxic) release', 'Small harmful (toxic) release'), ('Large (>1000m3) harmful (toxic) release', 'Large (>1000m3) harmful (toxic) release')], max_length=100, verbose_name='11b: Vapour emission')),
            ],
            options={
                'verbose_name': 'Consequence Factor Data',
                'verbose_name_plural': 'Consequence Factor Data',
            },
        ),
        migrations.CreateModel(
            name='InspectionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_inspection', models.DateField()),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_1', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 1')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_2', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 2')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_3', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 3')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_4', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 4')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_5', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 5')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_6', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 6')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_7', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 7')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_8', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 8')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_9', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 9')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_10', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 10')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_11', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 11')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_12', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 12')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_13', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 13')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_14', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 14')),
                ('minimum_thickness_measured_during_previous_inspection_for_shell_plate_15', models.CharField(max_length=100, verbose_name='18B: Minimum thickness measured during previous inspection for shell plate15')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_1', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 1')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_2', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 2')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_3', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 3')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_4', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 4')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_5', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 5')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_6', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 6')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_7', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 7')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_8', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 8')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_9', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 9')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_10', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 10')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_11', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 11')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_12', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 12')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_13', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 13')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_14', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 14')),
                ('minimum_thickness_measured_during_present_inspection_for_shell_plate_15', models.CharField(max_length=100, verbose_name='18C: Minimum thickness measured during present inspection for shell plate 15')),
                ('minimum_allowable_thickness_for_shell_plate_1', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 1')),
                ('minimum_allowable_thickness_for_shell_plate_2', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 2')),
                ('minimum_allowable_thickness_for_shell_plate_3', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 3')),
                ('minimum_allowable_thickness_for_shell_plate_4', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 4')),
                ('minimum_allowable_thickness_for_shell_plate_5', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 5')),
                ('minimum_allowable_thickness_for_shell_plate_6', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 6')),
                ('minimum_allowable_thickness_for_shell_plate_7', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 7')),
                ('minimum_allowable_thickness_for_shell_plate_8', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 8')),
                ('minimum_allowable_thickness_for_shell_plate_9', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 9')),
                ('minimum_allowable_thickness_for_shell_plate_10', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 10')),
                ('minimum_allowable_thickness_for_shell_plate_11', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 11')),
                ('minimum_allowable_thickness_for_shell_plate_12', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 12')),
                ('minimum_allowable_thickness_for_shell_plate_13', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 13')),
                ('minimum_allowable_thickness_for_shell_plate_14', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 14')),
                ('minimum_allowable_thickness_for_shell_plate_15', models.CharField(max_length=100, verbose_name='18D: Minimum allowable thickness for shell plate 15')),
                ('estimated_corrosion_for_shell_plate_1', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 1')),
                ('estimated_corrosion_for_shell_plate_2', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 2')),
                ('estimated_corrosion_for_shell_plate_3', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 3')),
                ('estimated_corrosion_for_shell_plate_4', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 4')),
                ('estimated_corrosion_for_shell_plate_5', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 5')),
                ('estimated_corrosion_for_shell_plate_6', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 6')),
                ('estimated_corrosion_for_shell_plate_7', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 7')),
                ('estimated_corrosion_for_shell_plate_8', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 8')),
                ('estimated_corrosion_for_shell_plate_9', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 9')),
                ('estimated_corrosion_for_shell_plate_10', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 10')),
                ('estimated_corrosion_for_shell_plate_11', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 11')),
                ('estimated_corrosion_for_shell_plate_12', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 12')),
                ('estimated_corrosion_for_shell_plate_13', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 13')),
                ('estimated_corrosion_for_shell_plate_14', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 14')),
                ('estimated_corrosion_for_shell_plate_15', models.CharField(max_length=100, verbose_name='18E: Estimated corrosion for shell plate 15')),
                ('NDT_method_used_for_thickness_measurements', models.CharField(choices=[('Crawler/beetle + US', 'Crawler /beetle + US'), ('US on gridline system', 'US on gridline system'), ('Visual + Spot ultrasonic (US)', 'Visual + Spot ultrasonic (US)')], max_length=100, verbose_name='24: NDT method used for thickness measurements')),
                ('frequency_of_internal_inspections_performed_during_service_life', models.CharField(choices=[('Multiple inspections carried out', 'Multiple inspections carried out'), ('No or minimal inspection data available', 'No or minimal inspection data available')], max_length=100, verbose_name='25: Frequency of internal inspections performed during service life')),
                ('corrosion_on_wind_girders', models.CharField(choices=[('No corrosion on wind girders', 'No corrosion on wind girders'), ('Corrosion present but no effect on the integrity of tankk sheel plates', 'Corrosion present but no effect on the integrity of tankk shell plates'), ('Corrosion present and induces effect on integrity of tank sheel plates', 'Corrosion present and induces effect on integrity of tank shell plates')], max_length=100, verbose_name='26: Corrosion on wind girders')),
                ('buckles_in_shell_plates', models.CharField(choices=[('No buckles on tank shell plates', 'No buckles on tank shell plates'), ('Buckles present but no effect on the integrity of tank shell plates', 'Buckles present but no effect on the integrity of tank shell plates'), ('Buckles present and induces effect on integrity of tank sheel plates', 'Buckles present and induces effect on integrity of tank shell plates')], max_length=100, verbose_name='27: Buckles in shell plates')),
                ('differential_setllement_between_tank_structure_and_piping_support', models.CharField(choices=[('No moments in shell nozzles or structures available which reduce nozzle loads', 'No moments in shell nozzles or structures available which reduce nozzle loads'), ('Moments present, but no effect on integrity of tank shell plates', 'Moments present, but no effect on integrity of tank shell plates'), ('Moments present and they induce effects on integrity of tank shell plates', 'Moments present and they induce effects on integrity of tank shell plates')], max_length=100, verbose_name='28: Differential setllement between tank structure and piping support')),
            ],
            options={
                'verbose_name': 'Inspection Data',
                'verbose_name_plural': 'Inspection Data',
            },
        ),
        migrations.CreateModel(
            name='ProbabilityFactorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impressed_coating_applied_to_sheel_plates', models.CharField(choices=[('Internal coating applied and quality is sound', 'Internal coating applied and quality is sound'), ('Internal coating applied and quality is poor', 'Internal coating applied and quality is poor'), ('Internal coating not existing', 'Internal coating not existing')], max_length=100, verbose_name='1: Impressed coating applied to sheel plates')),
                ('external_coating_applied_to_shell_plates', models.CharField(choices=[('External coating applied and quality is sound', 'External coating applied and quality is sound'), ('External coating applied and quality is poor', 'External coating applied and quality is poor'), ('External coating not existing', 'External coating not existing')], max_length=100, verbose_name='2: External coating applied to shell plates')),
                ('storage_conditions', models.CharField(choices=[('Temperature of product < 40°C', 'Temperature of product < 40°C'), ('40°C Temperature of product < 85°C', '40°C Temperature of product < 85°C'), ('Temperature of product > 85{DEGREE_SIGN}C', 'Temperature of product > 85°C')], max_length=100, verbose_name='3a: Storage conditions')),
                ('heating_coils_in_tank', models.CharField(choices=[('No heating coil or no contact between heating coil and shell plates', 'No heating coil or no contact between heating coil and shell plates'), ('Presence of heating coil in direct contact with shell plates', 'Presence of heating coil in direct contact with shell plates')], max_length=100, verbose_name='3b: Heating coils in tank')),
                ('product_corrosivity', models.CharField(choices=[('Product group 4', 'Product group 4'), ('Product group 5', 'Product group 5'), ('Product group 3', 'Product group 3'), ('Product group 6', 'Product group 6'), ('Product group 1', 'Product group 1')], max_length=100, verbose_name='4: product corrosivity')),
                ('vapour_corrosivity', models.CharField(choices=[('Vapour group 4', 'Vapour group 4'), ('Vapour group 5', 'Vapour group 5'), ('Vapour group 3', 'Vapour group 3'), ('Vapour group 6', 'Vapour group 6'), ('Vapour group 1', 'Vapour group 1')], max_length=100, verbose_name='5: Vapour Corrosivity')),
                ('corrosion_under_insulation_CUI', models.CharField(choices=[('Tank shell is not insulated', 'Tank shell is not insulated'), ('Tank shell is properly insulated and CUI is unlikely to occur', 'Tank shell is properly insulated and CUI is unlikely to occur'), ('CUI is likely to occur', 'CUI is likely to occur')], max_length=100, verbose_name='6: Corrosion under insulation (CUI)')),
            ],
            options={
                'verbose_name': 'Probability Factor Data',
                'verbose_name_plural': 'Probability Factor Data',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability_factor', models.CharField(max_length=50)),
                ('probability_rating', models.CharField(max_length=50)),
                ('economic_aspects_consequence_factor', models.CharField(max_length=50)),
                ('economic_aspects_consequence_rating', models.CharField(max_length=50)),
                ('health_and_safety_aspects_consequence_factor', models.CharField(max_length=50)),
                ('health_and_safety_aspects_consequence_rating', models.CharField(max_length=50)),
                ('environmental_aspects_consequence_factor', models.CharField(max_length=50)),
                ('environmental_aspects_consequence_rating', models.CharField(max_length=50)),
                ('overall_consequence_factor', models.CharField(max_length=50)),
                ('overall_consequence_rating', models.CharField(max_length=50)),
                ('risk_rating', models.CharField(max_length=50)),
                ('critical_shell_place', models.CharField(max_length=50)),
                ('corrosion_rate', models.CharField(max_length=50)),
                ('acceleration_factor_for_pitting', models.CharField(max_length=50)),
                ('adjusted_corrosion_rate', models.CharField(max_length=50)),
                ('remaining_life', models.CharField(max_length=50)),
                ('confidence_factor', models.CharField(max_length=50)),
                ('confidence_factor_adjustement', models.CharField(max_length=50)),
                ('ajusted_confidence_factor', models.CharField(max_length=50)),
                ('interval_before_next_required_inspection', models.CharField(max_length=50)),
                ('next_inspection', models.DateField()),
            ],
            options={
                'verbose_name': 'Results',
                'verbose_name_plural': 'Results',
            },
        ),
    ]
