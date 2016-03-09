import urllib2
from   urllib2 import Request, urlopen, URLError, HTTPError

class Request:
    def __init__(self, url):
        ''' Constructor for this class. '''
        # Initializer
        self.url = url

    def getHtmlfromUrl(self):
        print("Executing request for url : %s" % self.url)
        req = urllib2.Request(self.url)
        try:
            response = urllib2.urlopen(req)
        except HTTPError as e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        except URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        else:
            return response.read()