import locationtagger
from geopy.geocoders import Nominatim


def get_country(param):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(param)
    place_entity = locationtagger.find_locations(text=location[0])
    return check_entity(place_entity.countries)


def check_entity(list_param):
    lower_list = [ele.lower() for ele in list_param]
    return max(set(lower_list), key = lower_list.count)


def locate_text(param, flag=False):
    place_entity = locationtagger.find_locations(text=param)
    data = dict()
    # getting all countries
    print("The countries in text : ")
    print(place_entity.countries)
    if place_entity.countries:
        data['Country'] = check_entity(place_entity.countries)
        if flag==True:
            return data['Country']

    # getting all states
    print("The states in text : ")
    print(place_entity.regions)
    if place_entity.regions:
        data['Region'] = check_entity(place_entity.regions)

    # getting all cities
    print("The cities in text : ")
    print(place_entity.cities)
    if place_entity.cities:
        data['City'] = check_entity(place_entity.cities)

    if data:
        if data.get('Country'):
            return data
        elif data.get('City'):
            data['Country'] = get_country(data.get('City'))
            return data
        elif data.get('Region'):
            data['Country'] = get_country(data.get('Region'))
            return data
        else:
            return data
    else:
        return None


if __name__ == '__main__':
    sample_text = "India has very rich and vivid culture\
           widely spread from Kerala to Nagaland to Haryana to Maharashtra. " \
                  "Delhi being capital with Mumbai financial capital.\
                  Can be said better than some western cities such as " \
                  " Munich, London etc. Pakistan and Bangladesh share its borders"

    locate_text(sample_text)
