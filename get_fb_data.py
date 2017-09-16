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

    def print_page_data(self, places, number_of_pages=1):
        for place in places['data']:
            try:
                if place['emails'] and place['location']['country'] == 'United States':
                    print '{}, {}, {}'.format( ','.join(place['emails']), place['name'], place['location']['city'])
            except:
                pass
        print "----------------"


if __name__ == '__main__':
    fb1 = FacebookData()
    pages = fb1.search_for_pages('Indian Grocery Michigan')
    fb1.print_page_data(pages, 5)

