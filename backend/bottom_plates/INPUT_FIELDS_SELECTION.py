
#PROBABILITY FACTOR DATA BOTTOM PLATES
# Action Taken to Limit Corrosion on Bottom Plates

IMPRE_CATHODIC_PROTECTION = [
    ('All readings around the periphery > 0.85 V - Score=0', 'All readings around the periphery > 0.85 V'),
    ('0.6 V < All readings around the periphery < 0.85 V - Score=1', '0.6 V < All readings around the periphery < 0.85 V'),
    ('All readings around periphery < 0.6 V or none installed - Score=2', 'All readings around periphery < 0.6 V or none installed')
]
SACRIFICIAL_CATHODIC_PROPECTION = [
    ('Sacrificial CP available and operating - Score=0', 'Sacrificial CP available and operating'),
    ('Sacrificial CP not applicable - Score=0', 'Sacrificial CP not applicable'),
    ('Sacrificial CP not available and not operating - Score=2', 'Sacrificial CP not available and not operating')
]
BOTTOM_PLATES_INTERNAL_COATING_OR_LINING = [
    ('Internal coating applied and quality is sound - Score=0', 'Internal coating applied and quality is sound'),
    ('Internal coating applied but quality is poor - Score=1', 'Internal coating applied but quality is poor'),
    ('Not existing - Score=2', 'Not existing')
]
BOTTOM_PLATES_EXTERNAL_COATING = [
    ('External coating applied and quality is sound - Score=0', 'External coating applied and quality is sound'),
    ('External coating applied but quality is poor - Score=1', 'External coating applied but quality is poor'),
    ('Not existing - Score=2', 'Not existing')
]



# Features That Influences The Failure Mechanism of Bottom Plates

DEGREE_SIGN = u'\N{DEGREE SIGN}'

STORAGE_CONDITIONS = [
    (f'Temperature of product < 40{DEGREE_SIGN}C - Score=0', f'Temperature of product < 40{DEGREE_SIGN}C'),
    (f'40{DEGREE_SIGN}C Temperature of product < 85{DEGREE_SIGN}C - Score=1', f'40{DEGREE_SIGN}C Temperature of product < 85{DEGREE_SIGN}C'),
    (f'Temperature of product > 85{DEGREE_SIGN}C - Score=2', f'Temperature of product > 85{DEGREE_SIGN}C')
]
TYPE_OF_BOTTOM = [
    ('Cone up - Score=0', 'Cone up'),
    ('Flat - Score=2', 'Flat'),
    ('Cone down - Score=2', 'Cone down')
]
HEATING_COILS_IN_TANK = [
    ('No heating coil or no contact between heating coil and bottom plates - Score=0', 'No heating coil or no contact between heating coil and bottom plates'),
    ('Presence of heating coil in direct contact with bottom plates - Score=1', 'Presence of heating coil in direct contact with bottom plates')
]
PRODUCT_CORROSIVITY = [
    ('Group 1/Risk H - Score=2', 'Group 1/Risk H'),
    ('Group 3/Risk M - Score=1', 'Group 3/Risk M'),
    ('Group 4/Risk L - Score=0', 'Group 4/Risk L'),
    ('Group 5/Risk L - Score=0', 'Group 5/Risk L'),
    ('Group 6/Risk M - Score=1', 'Group 6/Risk M')
]



# Effectiveness of Drainage To Prevent Water Ingress 
# Under Bottom Plates

FOUNDATION_TYPE = [
    ('Piled concrete raft - Score=0', 'Piled concrete raft'),
    ('Concrete raft under tank - Score=0', 'Concrete raft under tank'),
    ('Sand pad with annular ring of coarse granular material + sound sand-bitumen top layer - Score=2/3', 'Sand pad with annular ring of coarse granular material + sound sand-bitumen top layer'),
    ('Sand pad with annular ring of coarse granular material - Score=4/3', 'Sand pad with annular ring of coarse granular material'),
    ('Traditional granular soil/sand type - Score=2', 'Traditional granular soil/sand type')
]
HEIGHT_OF_FOUNDATION = [
    ('Tank bottom free from contact with water - Score=0', 'Tank bottom free from contact with water'),
    ('Tank bottom in contact with water - Score=2', 'Tank bottom in contact with water')
]
EFFECTIVENESS_OF_DRAINAGE = [
    ('Slope of tank pad shoulder allows for adequate drainage away from tank bottom - Score=0', 'Slope of tank pad shoulder allows for adequate drainage away from tank bottom'),
    ('Water will remain under the tank bottom due to inadequate drainage or tank bottom is standing in water - Score=2', 'Water will remain under the tank bottom due to inadequate drainage or tank bottom is standing in water')
]





# CONSEQUENCE FACTOR DATA BOTTOM PLATES

# Economic Aspects

TIME_TO_REPAIR = [
    ('No internal entry required limited repair, no limitation on repair time - Score=1', 'No internal entry required limited repair, no limitation on repair time'),
    ('Internal entry required, major repair (<3 months) - Score=2', 'Internal entry required, major repair (<3 months)'),
    ('Internal entry required, major repair (3-8 months)- Score=3', 'Internal entry required, major repair (3-8 months)'),
    ('Internal entry required, limited repair (>8 months)- Score=4', 'Internal entry required, limited repair (>8 months)')
]
COST_OF_REPAIR = [
    ('Negligible or less than 5% of capital cost - Score=1', 'Negligible or less than 5% of capital cost'),
    ('5-10% of capital cost - Score=2', '5-10% of capital cost'),
    ('10-50% of capital cost - Score=3', '10-50% of capital cost'),
    ('>50% of capital cost (new tank) - Score=4', '>50% of capital cost (new tank)')
]
PROBABLE_MAGNITUDE_OF_PRODUCT_LOSS = [
    ('No release of product - Score=1', 'No release of product'),
    ('<5% of tank contents - Score=2', '<5% of tank contents'),
    ('>5% of tank contents - Score=3', '>5% of tank contents')
]


# Health and Safety Aspects

LIKELIHOOD_OF_INJURY_TO_PERSONNEL = [
    ('No injury or near miss - Score=1', 'No injury or near miss'),
    ('Minor injury - Score=2', 'Minor injury'),
    ('Lost time injury/Medical treatment - Score=3', 'Lost time injury/Medical treatment'),
    ('Seriuos injury/fatality on site - Score=4', 'Seriuos injury/fatality on site')
]
PRODUCT_FLAMMABILITY_AS_PER_MCSP = [
    ('Class III(1) and unclassified product - Score=1', 'Class III(1) and unclassified product'),
    ('Class II(1) product - Score=2', 'Class II(1) product'),
    ('Class II(2) and III(2) product - Score=3', 'Class II(2) and III(2) product'),
    ('Class I product - Score=4', 'Class I product'),
]
PRODUCT_TOXICITY = [
    ('Non-toxic substances- Score=1', 'Non-toxic substances'),
    ('Toxic substance if in contact with other substances - Score=2', 'Toxic substance if in contact with other substances'),
    ('Toxic substance - Score=3', 'Toxic substance'),
    ('Extremely toxic substance - Score=4', 'Extremely toxic substance')
]
LOCATION_OF_TANK_FARM = [
    ('Tank farm within an abandonned area - Score=1', 'Tank farm within an abandonned area'),
    ('Flat tank farm - Score=2', 'Flat tank farm'),
    ('Sloping tank farm - Score=3', 'Sloping tank farm'),
    ('In plant area within populous area - Score=4', 'In plant area within populous area')
]
# CONTINUED_LOCATION_OF_TANK_FARM = [
    # ('No public fence near tank farm', 'No public fence near tank farm'),
    # ('Presence of public fence near tank farm', 'Presence of public fence near tank farm')
# ]


# Environmental Aspects
ENVIRONMETAL_HAZARD_TO_SOIL_AND_WATER_AS_THE_POTENTIAL_TO_CAUSE = [
    ('Nor or negligle environment effect - Score=1', 'Nor or negligle environment effect'),
    ('Environmental nuisance affecting neighbourhood - Score=2', 'Environmental nuisance affecting neighbourhood'),
    ('Environmental pollution/Extensive restoration required - Score=3', 'Environmental pollution/Extensive restoration required'),
    ('Severe demage/nuisance/pollution over large area- Score=4', 'Severe demage/nuisance/pollution over large area')
]
VAPOUR_EMISSION = [
    ('No or negligle harmful (toxic) release - Score=1', 'No or negligle harmful (toxic) release'),
    ('Small harmful (toxic) release - Score=2', 'Small harmful (toxic) release'),
    ('Large (>1000m3) harmful (toxic) release - Score=3', 'Large (>1000m3) harmful (toxic) release')
]




# INSPECTION DATA 
ACCELERATION_FACTOR_FOR_PITTING = [
    ('CR ≥ 0.5mm (0.020 in.) /year - Score=1.15', 'CR ≥ 0.5mm (0.020 in.) /year'),
    ('0.3 mm (0.013 in.) ≤ CR < 0.5mm (0.020 in.) /year - Score=1.1', '0.3 mm (0.013 in.) ≤ CR < 0.5mm (0.020 in.) /year'),
    ('0.1 mm (0.004 in.) ≤ CR < 0.3mm (0.013 in.) /year - Score=1.05', '0.1 mm (0.004 in.) ≤ CR < 0.3mm (0.013 in.) /year'),
    ('CR < 0.1mm (0.004 in.)/year - Score=1.0', 'CR < 0.1mm (0.004 in.)/year')
]

# Inspections
NDT_METHOD_USED_FOR_THICKNESS_MEASUREMENTS = [
    ('Floor scan + US - Score=-0.1', 'Floor scan + US'),
    ('US on gridline system - Score=0', 'US on gridline system'),
    ('Visual + Spot ultrasonic (US) - Score=0.1)', 'Visual + Spot ultrasonic (US)')
]
FREQUENCY_OF_INTERNAL_INSPECTIONS_PERFORMED_DURING_SERVICE_LIFE = [
    ('Multiple inspections carried out - Score=0.1', 'Multiple inspections carried out'),
    ('No or minimal inspection data available - Score=0', 'No or minimal inspection data available')
]
TYPE_OF_INTERCONNECTING_BOTTOM_PLATE_WELDS_OUTSIDE_OF_ANNULAR_SECTION = [
    ('Butt welds - Score=0.1', 'Butt welds'),
    ('Double pass lap welds - Score=0', 'Double pass lap welds'),
    ('Single pass lap welds - Score=-0.1', 'Single pass lap welds')
]

