from .models import WebImage, WebPage

class AssignmentMainResponse(object):
    success = None
    error = None
    data = None
    status = None


class WebImageResponse(object):
    image_url = []

    def __init__(self, link):
        self.image_url = link


class ImageDataResponse(object):
    web_page_urls = []

    def __init__(self, urls):

        for link in urls:
            self.web_url = link.web_page.crawled_url
            self.web_page_urls.append( WebImageResponse(link))



class WebPageDataResponse(object):
    web_page_url = None
    image_urls = []

    def __init__(self, web_urls):
        self.links = []
        
        for url in web_urls:
            self.web_page_url = url.crawled_url
            self.image_urls.append(ImageDataResponse(url.webimage_set.all()))

    