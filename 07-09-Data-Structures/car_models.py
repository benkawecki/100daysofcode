cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    jeep_list = cars['Jeep']
    jeep_string = ''
    for car in jeep_list:
        jeep_string = jeep_string+car+', '
    return jeep_string[:-2]



def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    firsts = []
    for k,v in cars.items():
        firsts.append(v[0])
    return firsts

def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matching = []
    for k,v in cars.items():
        for models in v:
            if models.lower().find(grep) >= 0:
                matching.append(models)
    return matching


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for k,v in cars.items():
        v.sort()
    return cars

if __name__ == "__main__":
    print(get_all_jeeps())
    print(get_first_model_each_manufacturer())
    print(get_all_matching_models())
    print(sort_car_models())
