from geopy.distance import geodesic
from opencage.geocoder import OpenCageGeocode


def find_distance(A, B):
    key = 'dabcd57e3a714a138b617b172ed7f3c2'  # get api key from:  https://opencagedata.com
    geocoder = OpenCageGeocode(key)

    result_A = geocoder.geocode(A)
    lat_A = result_A[0]['geometry']['lat']
    lng_A = result_A[0]['geometry']['lng']

    result_B = geocoder.geocode(B)
    lat_B = result_B[0]['geometry']['lat']
    lng_B = result_B[0]['geometry']['lng']

    return str(round(geodesic((lat_A, lng_A), (lat_B, lng_B)).kilometers))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def definePrice(distance):
    return ((distance*5)/100)*1.9



def getUser():
    pass
