import json
import crud, model, server
import requests

import os
key_1 = os.environ['API_KEY_1']

os.system('dropdb cropweather')
os.system('createdb cropweather')

model.connect_to_db(server.app)
model.db.create_all()

res = requests.get(
        f'http://harvesthelper.herokuapp.com/api/v1/plants?api_key={key_1}')

crop_data = res.json()

crops_in_db = []

for crop in crop_data:
    crop_id = crop['id']
    crop_name = crop['name']
    crop_description = crop['description']
    crop_sun = crop['optimal_sun']
    crop_soil = crop['optimal_soil']
    crop_planting_considerations = crop['planting_considerations']
    crop_when_to_plant = crop['when_to_plant']
    crop_transplanting = crop['transplanting']
    crop_growing_from_seed = crop['growing_from_seed']
    crop_spacing = crop['spacing']
    crop_watering = crop['watering']
    crop_feeding = crop['feeding']
    crop_other_care = crop['other_care']
    crop_diseases = crop['diseases']
    crop_pests = crop['pests']
    crop_harvesting = crop['harvesting']
    crop_storage_use = crop['storage_use']
    crop_image_url = crop['image_url']

    db_crop = crud.create_crop(crop_id, crop_name, crop_description, crop_sun, 
        crop_soil, crop_planting_considerations, crop_when_to_plant, crop_transplanting,
        crop_growing_from_seed, crop_spacing, crop_watering, crop_feeding, 
        crop_other_care, crop_diseases, crop_pests, crop_harvesting, 
        crop_storage_use, crop_image_url)

    crops_in_db.append(db_crop)


with open('data/crop_conditions.json') as f:
    crop_condition_data = json.loads(f.read())

crop_conditions_in_db = []

for crop_condition in crop_condition_data:
    crop_id = crop_condition['id']
    crop_name = crop_condition['crop name']
    plant_hardiness_zone = crop_condition['zone']
    planting_month = crop_condition['planting month']
    shade_ok = crop_condition['shade ok']
    soil_type = crop_condition['soil type']
    difficulty = crop_condition['difficulty']

    db_crop_condition = crud.create_crop_conditions(crop_id,
        crop_name, plant_hardiness_zone, planting_month, shade_ok, soil_type, difficulty)

    crop_conditions_in_db.append(db_crop_condition)

