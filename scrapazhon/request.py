import urllib2
from   urllib2 import Request, urlopen, URLError, HTTPError

class Request:
    def __init__(self, url):
        ''' Constructor for this class. '''
        # Initializer
        self.url = url

    def get_html_from_url(self):
        print("Executing request for url : %s" % self.url)
        try:
            response = self.url_opener().open(self.url)
        except HTTPError as e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            raise HTTPError, e.code
        except URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            raise URLError, e.reason
        else:
            return { "code" : response.code, "response" : response.read() }

    def url_opener(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        return opener