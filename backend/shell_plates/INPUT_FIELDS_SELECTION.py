
IMPRESSED_COATING_APPLIED_TO_SHEEL_PLATES = [
    ('Internal coating applied and quality is sound', 'Internal coating applied and quality is sound'),
    ('Internal coating applied and quality is poor', 'Internal coating applied and quality is poor'),
    ('Internal coating not existing', 'Internal coating not existing')
]
EXTERNAL_COATING_APPLIED_TO_SHELL_PLATES = [
    ('External coating applied and quality is sound', 'External coating applied and quality is sound'),
    ('External coating applied and quality is poor', 'External coating applied and quality is poor'),
    ('External coating not existing', 'External coating not existing')
]




DEGREE_SIGN = u'\N{DEGREE SIGN}'

STORAGE_CONDITIONS = [
    (f'Temperature of product < 40{DEGREE_SIGN}C', f'Temperature of product < 40{DEGREE_SIGN}C'),
    (f'40{DEGREE_SIGN}C Temperature of product < 85{DEGREE_SIGN}C', f'40{DEGREE_SIGN}C Temperature of product < 85{DEGREE_SIGN}C'),
    ('Temperature of product > 85{DEGREE_SIGN}C', f'Temperature of product > 85{DEGREE_SIGN}C')
]
HEATING_COILS_IN_TANK = [
    ('No heating coil or no contact between heating coil and shell plates', 'No heating coil or no contact between heating coil and shell plates'),
    ('Presence of heating coil in direct contact with shell plates', 'Presence of heating coil in direct contact with shell plates')
]
PRODUCT_CORROSIVITY = [
    ('Product group 4', 'Product group 4'),
    ('Product group 5', 'Product group 5'),
    ('Product group 3', 'Product group 3'),
    ('Product group 6', 'Product group 6'),
    ('Product group 1', 'Product group 1')
]
VAPOUR_CORROSIVITY = [
    ('Vapour group 4', 'Vapour group 4'),
    ('Vapour group 5', 'Vapour group 5'),
    ('Vapour group 3', 'Vapour group 3'),
    ('Vapour group 6', 'Vapour group 6'),
    ('Vapour group 1', 'Vapour group 1')
]
CORROSION_UNDER_INSULATION_CUI = [
    ('Tank shell is not insulated', 'Tank shell is not insulated'),
    ('Tank shell is properly insulated and CUI is unlikely to occur', 'Tank shell is properly insulated and CUI is unlikely to occur'),
    ('CUI is likely to occur', 'CUI is likely to occur')
]





TIME_TO_REPAIR = [
    ('No internal entry required, limited repair, no limitation on repair time', 'No internal entry required, limited repair, no limitation on repair time'),
    ('Internal entry required, limited repair (<3 months)', 'Internal entry required, limited repair (<3 months)'),
    ('Internal entry required, major repair (3-8 months)', 'Internal entry required, major repair (3-8 months)'),
    ('Internal entry required, major repair (>8 months)', 'Internal entry required, major repair (>8 months)')
]
COST_OF_REPAIR = [
    ('Negligible or less than 5% of capital cost', 'Negligible or less than 5% of capital cost'),
    ('5-10% of capital cost', '5-10% of capital cost'),
    ('10-50% of capital cost', '10-50% of capital cost'),
    ('>50% of capital cost (new tank)', '>50% of capital cost (new tank)')
]
PROBABLE_MAGNITUDE_OF_PRODUCT_LOSS = [
    ('No release of product', 'No release of product'),
    ('<5% of tank contents', '<5% of tank contents'),
    ('>5% of tank contents', '>5% of tank contents')
]



LIKELIHOOD_OF_INJURY_TO_PERSONNEL = [
    ('No injury or near miss', 'No injury or near miss'),
    ('Minor injury', 'Minor injury'),
    ('Lost time injury/Medical treatment', 'Lost time injury/Medical treatment'),
    ('Serious injury/fatality on site', 'Serious injury/fatality on site')
]
PRODUCT_FLAMMABILITY_AS_PER_MCSP = [
    ('Class III(1) and unclassified product', 'Class III(1) and unclassified product'),
    ('Class II(1) product', 'Class II(1) product'),
    ('Class II(2) and III(2) product', 'Class II(2) and III(2) product'),
    ('Class I product', 'Class I product'),
]
PRODUCT_TOXICITY = [
    ('Non-toxic substances', 'Non-toxic substances'),
    ('Toxic substance if in contact with other substances', 'Toxic substance if in contact with other substances'),
    ('Toxic substance', 'Toxic substance'),
    ('Extremely toxic substance', 'Extremely toxic substance')
]
LOCATION_OF_TANK_FARM = [
    ('Tank farm within an abandonned area', 'Tank farm within an abandonned area'),
    ('Flat tank farm', 'Flat tank farm'),
    ('Flopping tank farm', 'Flopping tank farm'),
    ('In plant area within populous area', 'In plant area within populous area')
]
CONTINUED_LOCATION_OF_TANK_FARM = [
    ('No public fence near tank farm', 'No public fence near tank farm'),
    ('Presence of public fence near tank farm', 'Presence of public fence near tank farm')
]





# Environmental Aspects
ENVIRONMETAL_HAZARD_TO_SOIL_AND_WATER_AS_THE_POTENTIAL_TO_CAUSE = [
    ('No or negligle environment effect', 'No or negligle environment effect'),
    ('Environmental nuisance affecting neighbourhood', 'Environmental nuisance affecting neighbourhood'),
    ('Environmental pollution/Extensive restoration required', 'Environmental pollution/Extensive restoration required'),
    ('Severe demage/nuisance/pollution over large area', 'Severe demage/nuisance/pollution over large area')
]
VAPOUR_EMISSION = [
    ('No or negligle harmful (toxic) release', 'No or negligle harmful (toxic) release'),
    ('Small harmful (toxic) release', 'Small harmful (toxic) release'),
    ('Large (>1000m3) harmful (toxic) release', 'Large (>1000m3) harmful (toxic) release')
]



NDT_METHOD_USED_FOR_THICKNESS_MEASUREMENTS = [
    ('Crawler/beetle + US', 'Crawler /beetle + US'),
    ('US on gridline system', 'US on gridline system'),
    ('Visual + Spot ultrasonic (US)', 'Visual + Spot ultrasonic (US)')
]
FREQUENCY_OF_INTERNAL_INSPECTIONS_PERFORMED_DURING_SERVICE_LIFE = [
    ('Multiple inspections carried out', 'Multiple inspections carried out'),
    ('No or minimal inspection data available', 'No or minimal inspection data available')
]
CORROSION_ON_WIND_GIRDERS = [
    ('No corrosion on wind girders', 'No corrosion on wind girders'),
    ('Corrosion present but no effect on the integrity of tankk sheel plates', 'Corrosion present but no effect on the integrity of tankk shell plates'),
    ('Corrosion present and induces effect on integrity of tank sheel plates', 'Corrosion present and induces effect on integrity of tank shell plates')
]
BUCKLES_IN_SHELL_PLATES = [
    ('No buckles on tank shell plates', 'No buckles on tank shell plates'),
    ('Buckles present but no effect on the integrity of tank shell plates', 'Buckles present but no effect on the integrity of tank shell plates'),
    ('Buckles present and induces effect on integrity of tank sheel plates', 'Buckles present and induces effect on integrity of tank shell plates')
]
DIFFERENTIAL_SETLLEMENT_BETWEEN_TANK_STRUCTURE_AND_PIPING_SUPPORT = [
    ('No moments in shell nozzles or structures available which reduce nozzle loads', 'No moments in shell nozzles or structures available which reduce nozzle loads'),
    ('Moments present, but no effect on integrity of tank shell plates', 'Moments present, but no effect on integrity of tank shell plates'),
    ('Moments present and they induce effects on integrity of tank shell plates', 'Moments present and they induce effects on integrity of tank shell plates')
]









