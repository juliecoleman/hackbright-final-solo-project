"""CRUD operations."""

from model import db, Gardener, Crop, CropCondition, FavoriteCrop, connect_to_db

def create_gardener(username, password):
    """Create new gardener user."""

    gardener = Gardener(username=username, password=password)

    db.session.add(gardener)
    db.session.commit()

    return gardener

def create_crop(crop_id, crop_name, crop_description, crop_sun, crop_soil,
    crop_planting_considerations, crop_when_to_plant, crop_growing_from_seed,
    crop_transplanting, crop_spacing, crop_watering, crop_feeding, crop_other_care,
    crop_diseases, crop_pests, crop_harvesting, crop_storage_use, 
    crop_image_url):
    """Create and return a new crop."""

    crop = Crop(crop_id=crop_id, 
                  crop_name=crop_name, 
                  crop_description=crop_description, 
                  crop_sun=crop_sun,
                  crop_soil=crop_soil,
                  crop_planting_considerations=crop_planting_considerations,
                  crop_when_to_plant=crop_when_to_plant,
                  crop_growing_from_seed=crop_growing_from_seed,
                  crop_transplanting=crop_transplanting,
                  crop_spacing=crop_spacing,
                  crop_watering=crop_watering,
                  crop_feeding=crop_feeding,
                  crop_other_care=crop_other_care,
                  crop_diseases=crop_diseases,
                  crop_pests=crop_pests,
                  crop_harvesting=crop_harvesting,
                  crop_storage_use=crop_storage_use,
                  crop_image_url=crop_image_url)

    db.session.add(crop)
    db.session.commit()

    return crop

def create_crop_conditions(crop_id, crop_name, plant_hardiness_zone, 
                           planting_month, shade_ok, soil_type, 
                           soil_ph, difficulty):
    """Create and return counditions for a crop."""

    crop_condition = CropCondition(crop_id=crop_id,
                                    crop_name=crop_name,
                                    plant_hardiness_zone=plant_hardiness_zone,
                                    planting_month=planting_month,
                                    shade_ok=shade_ok,
                                    soil_type=soil_type,
                                    soil_ph=soil_ph,
                                    difficulty=difficulty)
    db.session.add(crop_condition)
    db.session.commit()

    return crop_condition

def create_favorite_crop(gardener_id, crop_id):
    """Save favorite crops."""
    # print('**************CRUD_ID', crop_id)
    favorite_crop = FavoriteCrop(gardener_id=gardener_id, crop_id=crop_id)

    db.session.add(favorite_crop)
    db.session.commit()

    return favorite_crop

def get_gardener_by_username(username):
    """Retrieve a gardener user by their username."""

    return Gardener.query.filter(Gardener.username == username).first()

def get_crop_recommendations(plant_hardiness_zone, planting_month, shade_ok, 
                             soil_type, soil_ph, difficulty):
    """Get crop recommendations based on gardener user inputs."""

    crop_list = []

    if planting_month == 'unknown':

        if plant_hardiness_zone == 'unknown':

            if shade_ok == 'unknown':

                if soil_ph == 'unknown':

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter().options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.soil_type == soil_type).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                else:

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.soil_type == soil_type,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

            else:

                if soil_ph == 'unknown':

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.shade_ok == shade_ok).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter( 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                else:

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter( 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter( 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()
        else:
            if shade_ok == 'unknown':

                if soil_ph == 'unknown':

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.soil_type == soil_type).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                else:

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.soil_type == soil_type,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

            else:

                if soil_ph == 'unknown':

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.shade_ok == shade_ok).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                else:

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

    else:

        if plant_hardiness_zone == 'unknown':

            if shade_ok == 'unknown':

                if soil_ph == 'unknown':

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_type == soil_type).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter( 
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                else:

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_type == soil_type,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

            else:

                if soil_ph == 'unknown':

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month, 
                                CropCondition.shade_ok == shade_ok).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month, 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                else:

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month, 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month, 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.planting_month == planting_month,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()
        else:
            if shade_ok == 'unknown':

                if soil_ph == 'unknown':

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.planting_month == planting_month).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_type == soil_type).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone, 
                                CropCondition.planting_month == planting_month,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone, 
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                else:

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_type == soil_type,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone, 
                                CropCondition.planting_month == planting_month,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone, 
                                CropCondition.planting_month == planting_month,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

            else:

                if soil_ph == 'unknown':

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.planting_month == planting_month, 
                                CropCondition.shade_ok == shade_ok).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.planting_month == planting_month, 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone, 
                                CropCondition.planting_month == planting_month,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone, 
                                CropCondition.planting_month == planting_month,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty).options(db.joinedload('crop')).all()


                else:

                    if difficulty == 'unknown':

                        if soil_type == 'unknown':
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.planting_month == planting_month, 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()


                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone,
                                CropCondition.planting_month == planting_month, 
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                    else:

                        if soil_type == 'unknown':

                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone, 
                                CropCondition.planting_month == planting_month,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()

                        else:
                            crop_recommendations = CropCondition.query.filter(
                                CropCondition.plant_hardiness_zone == plant_hardiness_zone, 
                                CropCondition.planting_month == planting_month,
                                CropCondition.shade_ok == shade_ok,
                                CropCondition.soil_type == soil_type,
                                CropCondition.difficulty == difficulty,
                                CropCondition.soil_ph == soil_ph).options(db.joinedload('crop')).all()



    for crop_recommendation in crop_recommendations:
        crop_dictionary = {}
        crop_dictionary['planting_month'] = crop_recommendation.planting_month
        crop_dictionary['shade_ok'] = crop_recommendation.shade_ok
        crop_dictionary['soil_type'] = crop_recommendation.soil_type
        crop_dictionary['soil_ph'] = crop_recommendation.soil_ph
        crop_dictionary['difficulty'] = crop_recommendation.difficulty
        crop_dictionary['name'] = crop_recommendation.crop_name
        crop_dictionary['planting_consideration'] = crop_recommendation.crop.crop_planting_considerations
        crop_dictionary['growing_from_seed'] = crop_recommendation.crop.crop_growing_from_seed
        crop_dictionary['transplanting'] = crop_recommendation.crop.crop_transplanting
        crop_dictionary['spacing'] = crop_recommendation.crop.crop_spacing
        crop_dictionary['watering'] = crop_recommendation.crop.crop_watering
        crop_dictionary['feeding'] = crop_recommendation.crop.crop_feeding
        crop_dictionary['crop_id'] = crop_recommendation.crop.crop_id
        crop_dictionary['image_url'] = crop_recommendation.crop.crop_image_url

        if crop_dictionary not in crop_list:
            crop_list.append(crop_dictionary)


    return crop_list

def get_crop_favorites(gardener_id):
    """Get favorite crops for a gardener user."""

    favorite_crop_list = []

    favorite_crops = FavoriteCrop.query.filter(
        FavoriteCrop.gardener_id == gardener_id).options(db.joinedload('crop')).all()
    # .joinedload('condition')

    for favorite_crop in favorite_crops:
        favorite_crop_dictionary = {}
        favorite_crop_dictionary['name'] = favorite_crop.crop.crop_name
        favorite_crop_dictionary['planting_consideration'] = favorite_crop.crop.crop_planting_considerations
        favorite_crop_dictionary['growing_from_seed'] = favorite_crop.crop.crop_growing_from_seed
        favorite_crop_dictionary['transplanting'] = favorite_crop.crop.crop_transplanting
        favorite_crop_dictionary['spacing'] = favorite_crop.crop.crop_spacing
        favorite_crop_dictionary['watering'] = favorite_crop.crop.crop_watering
        favorite_crop_dictionary['feeding'] = favorite_crop.crop.crop_feeding
        favorite_crop_dictionary['crop_id'] = favorite_crop.crop_id
        favorite_crop_dictionary['image_url'] = favorite_crop.crop.crop_image_url
        # favorite_crop_dictionary['shade_ok'] = favorite_crop.condition.shade_ok

        favorite_crop_list.append(favorite_crop_dictionary)

    return favorite_crop_list

def get_crop_conditions_shade_soil_difficulty():
    """Get crop conditions for shade, soil, and difficulty."""

    condition_list = []

    conditions = CropCondition.query.all()

    for condition in conditions:
        condition_dictionary = {}
        condition_dictionary['crop_id'] = condition.crop_id
        condition_dictionary['plant_hardiness_zone'] = condition.plant_hardiness_zone
        condition_dictionary['planting_month'] = condition.planting_month
        condition_dictionary['shade_ok'] = condition.shade_ok
        condition_dictionary['soil_type'] = condition.soil_type
        condition_dictionary['soil_ph'] = condition.soil_ph
        condition_dictionary['difficulty'] = condition.difficulty

        condition_list.append(condition_dictionary)

    condition_refined_dictionary = {}

    for condition in condition_list:

        if condition['crop_id'] not in condition_refined_dictionary:

            condition_refined_dictionary[condition['crop_id']] = {'shade_ok': condition['shade_ok'], 'soil_type': condition['soil_type'], 'soil_ph': condition['soil_ph'], 'difficulty': condition['difficulty']}      

    return condition_refined_dictionary


def get_crop_conditions_zone_month():
    """Get crop conditions for which months a crop can be planted in any given
    zone."""

    condition_list = []

    conditions = CropCondition.query.all()

    for condition in conditions:
        condition_dictionary = {}
        condition_dictionary['crop_id'] = condition.crop_id
        condition_dictionary['plant_hardiness_zone'] = condition.plant_hardiness_zone
        condition_dictionary['planting_month'] = condition.planting_month

        condition_list.append(condition_dictionary)

    condition_refined_dictionary_2 = {}

    for condition in condition_list:

        if condition['crop_id'] in condition_refined_dictionary_2:

            if condition['plant_hardiness_zone'] not in condition_refined_dictionary_2[condition['crop_id']]:

                condition_refined_dictionary_2[condition['crop_id']][condition['plant_hardiness_zone']] = [condition['planting_month']]
            else:

                if condition['planting_month'] not in condition_refined_dictionary_2[condition['crop_id']][condition['plant_hardiness_zone']]:

                    condition_refined_dictionary_2[condition['crop_id']][condition['plant_hardiness_zone']].append(condition['planting_month'])

        else:

            condition_refined_dictionary_2[condition['crop_id']] = {condition['plant_hardiness_zone']: [condition['planting_month']]}


    return condition_refined_dictionary_2



def check_crop_favorites(crop_id, gardener_id):
    """Check if crop is already in favorites."""

    return FavoriteCrop.query.filter(
        FavoriteCrop.crop_id == crop_id,
        FavoriteCrop.gardener_id == gardener_id).first()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)