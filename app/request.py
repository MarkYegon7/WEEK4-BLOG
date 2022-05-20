from .models import Quote
import urllib.request,json

def get_quote():
    base_url='http://quotes.stormconsultancy.co.uk/random.json'.format()
    with urllib.request.urlopen(base_url)as url:
        url_details_data=url.read()
        url_details_response=json.loads(url_details_data)

        url_object=None

        if url_details_response:
            author=url_details_response.get('author')
            quote=url_details_response.get('quote')

            url_object=Quote(author,quote)

        return url_object