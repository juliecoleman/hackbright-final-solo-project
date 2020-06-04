import json
import crud, model, server
import requests

import os
key_2 = os.environ['API_KEY_2']

os.system('dropdb cropweather')
os.system('createdb cropweather')

model.connect_to_db(server.app)
model.db.create_all()

res = requests.get(
        f'http://harvesthelper.herokuapp.com/api/v1/plants?api_key={key_2}')

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
        crop_soil, crop_planting_considerations, crop_when_to_plant, 
        crop_growing_from_seed, crop_spacing, crop_watering, crop_feeding, 
        crop_other_care, crop_diseases, crop_pests, crop_harvesting, 
        crop_storage_use, crop_image_url)

    crops_in_db.append(db_crop)

