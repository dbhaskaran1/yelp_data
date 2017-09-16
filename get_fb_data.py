import facebook
import requests
import ConfigParser


class FacebookData(object):
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read('config/client.cfg')

        access_token=config.get('fb','access_token')
        fb_api_version=config.get('fb','fb_api_version')

        self.graph = facebook.GraphAPI(
        access_token=access_token,
        version=fb_api_version)

    def search_for_pages(self, string_to_search_for):
        graph = self.graph
        pages = graph.search(
            type='page',
            q=string_to_search_for,
            center='0,0',
            distance=5000,
            fields='name, emails, location, about')

        return pages

    def iterate_through_pages(self, data):
        for place in data:
            try:
                if place['emails'] and place['location']['country'] == 'United States':
                    print '{}, {}, {}'.format( ','.join(place['emails']), place['name'], place['location']['city'])
            except:
                pass

    def print_page_data(self, places, number_of_pages=1):
        self.iterate_through_pages(places['data'])

        try:
            if number_of_pages > 1:
                number_of_pages -= 1
                pages = requests.get(places['paging']['next']).json()
                self.iterate_through_pages(pages['data'])
        except:
            pass

if __name__ == '__main__':
    fb1 = FacebookData()
    search_term = 'Indian Groceries'
    states_list1 = [ 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
					'Georgia', 'Hawaii', 'Idaho', 'Illinois Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
					'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana Nebraska', 'Nevada',
					'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
					'Oregon', 'Pennsylvania Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
					'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming' ]
    states_list = ['Texas', 'California']
    for state in states_list:
        pages = fb1.search_for_pages(search_term + state)
        fb1.print_page_data(pages, 20)
