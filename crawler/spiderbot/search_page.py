from html.parser import HTMLParser
from urllib import parse

class SearchLinks(HTMLParser):

    def __init__(self, homepage_url):
        super().__init__()
        self.homepage_url = homepage_url
        self.web_links = set()
        self.image_links = set() 

    def handle_starttag(self, tag, attrs):
        if(tag == 'a'):
            for (attr, val) in attrs:
                if(attr == 'href'):
                    link = parse.urljoin(self.homepage_url, val)
                    self.web_links.add(link)
                    print(link)

        if(tag == 'img'):
            for (attr, val) in attrs:
                if(attr == 'src'):
                    link = parse.urljoin(self.homepage_url, val)
                    self.image_links.add(link)
                    print(link)

    def error(self, message):
        pass

    
    def web_page_links(self):
        return self.web_links
    

    def web_page_image_links(self):
        return self.image_links