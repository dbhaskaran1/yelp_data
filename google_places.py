from googleplaces import GooglePlaces, types, lang
import csv

API_KEY = 'AIzaSyDJDB14qwvHFc3_3LSEUobrsZ6WUCnjNmQ'
super_market = types.TYPE_GROCERY_OR_SUPERMARKET
dept_store = types.TYPE_GROCERY_OR_SUPERMARKET

google_places = GooglePlaces(API_KEY)

#query_result = google_places.nearby_search(
#    location='Ann Arbor', keyword='Patels',
#    radius=1000, types=types.TYPE_GROCERY_OR_SUPERMARKET)

#if query_result.has_attributions:
#   print query_result.html_attributions

#for place in query_result.places:
#    print place.name
#    print place.geo_location
#    print place.place_id

csvfile = open('names.csv', 'a')
fieldnames = ['name', 'phone', 'website', 'address']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

query_result = google_places.text_search(
    location='Orlando', query='Indian Grocery',
    radius=1000, types=types.TYPE_GROCERY_OR_SUPERMARKET)

if query_result.has_attributions:
   print query_result.html_attributions

for place in query_result.places:
    place.get_details()

    writer.writerow({
        'name': place.name,
        'phone': place.local_phone_number,
        'website': place.website,
        'address': place.formatted_address
    })
