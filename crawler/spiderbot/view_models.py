from .models import WebImage, WebPage

class AssignmentMainResponse(object):
    success = None
    error = None
    data = None
    status = None


class WebImageResponse(object):
    image_url = None

    def __init__(self, link):
        self.image_url = link


class ImageDataResponse(object):
    
    web_url = None

    def __init__(self, crawled_url, urls):
        self.web_url = crawled_url
        self.web_image_urls = []
        for link in urls:
            
            self.web_image_urls.append( WebImageResponse(link.image_url))



class WebPageDataResponse(object):
    
    image_urls = []

    def __init__(self, web_urls):
        self.links = []
        
        for url in web_urls:
           
            self.image_urls.append(ImageDataResponse(url.crawled_url, url.webimage_set.all()))

    