from urllib.request import urlopen
from urllib.parse import urlparse
import urllib
from .search_page import SearchLinks
import spiderbot.constant as constant
from spiderbot.general import set_to_file
from .models import WebImage, WebPage


class WebCrawler:

    queue_link = set()
    crawled_link = set()

    queue_image = set()
    crawled_image = set()

    next_links = set()
    

    queue_file = "que.txt"
    crawled_file = "crawl.txt"

    image_queue_file = "que_image.txt"
    image_crawled_file = "crawl_image.txt"

    homepage_url = ""


    def __init__(self,homepage_url):
        WebCrawler.homepage_url = homepage_url
        self.crawl_web_page(WebCrawler.homepage_url)
        

    @staticmethod
    def crawl_web_page(page_link):
        gather_page_links = list(WebCrawler.fetch_web_links(page_link))
        
        if(len(gather_page_links) > 0 ):
            WebCrawler.next_links = gather_page_links[0]
            WebCrawler.add_web_links_to_queue(gather_page_links[0])
            WebCrawler.add_image_links_to_queue(gather_page_links[1])

            try:
                WebCrawler.queue_link.remove(page_link)
                WebCrawler.crawled_link.add(page_link)
            except:
                print("Could not remove web link")
            WebCrawler.update_files()
            web_page_obj = WebCrawler.add_link_to_db(page_link)
            WebCrawler.add_images_to_db(web_page_obj, gather_page_links[1])
           

    @staticmethod
    def fetch_web_links(page_link):
        html_string = ''
        try:
            hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
            req = urllib.request.Request(page_link, headers=hdr)
            response = urlopen(req)
            
            
            if 'text/html' in response.getheader('Content-Type') :
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = SearchLinks(WebCrawler.homepage_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            WebCrawler.add_error_to_log(page_link, str(e))
            WebCrawler.queue_link.remove(page_link)
            return list()
        return [finder.web_page_links(), finder.web_page_image_links()]
    


    @staticmethod
    def add_web_links_to_queue(links):
        for link in links:
            if(link in WebCrawler.queue_link or link in WebCrawler.crawled_link):
                continue
            if(urlparse(WebCrawler.homepage_url).netloc not in link):
                continue
            WebCrawler.queue_link.add(link)
            


    @staticmethod
    def add_image_links_to_queue(links):
        for link in links:
            if(link in WebCrawler.queue_image or link in WebCrawler.crawled_image):
                continue
            WebCrawler.queue_image.add(link)
            

    @staticmethod
    def update_files():
        set_to_file(WebCrawler.queue_link, WebCrawler.queue_file)
        set_to_file(WebCrawler.crawled_link, WebCrawler.crawled_file)

        set_to_file(WebCrawler.queue_image, WebCrawler.image_queue_file)
        set_to_file(WebCrawler.crawled_image, WebCrawler.image_crawled_file)
    
    @staticmethod
    def add_error_to_log(url, error_text):
        with open(constant.LOG_FILE,"w") as f:
            f.write("Error : \n")
            f.write(url+"\n" + error_text)
    
    @staticmethod
    def add_images_to_db(web_page_obj, image_links):

        for url in image_links:
            web_page_image_obj = WebImage(image_url = url, web_page = web_page_obj)
            web_page_image_obj.save()
        

    @staticmethod
    def add_link_to_db( page_link ):
        web_page_obj = WebPage(crawled_url = page_link)
        web_page_obj.save()
        return web_page_obj