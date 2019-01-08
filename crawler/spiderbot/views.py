from django.shortcuts import render

# Create your views here.

from .web_crawler import WebCrawler
import spiderbot.constant as constant
import threading
import time

def search_web():
    t = time.time()
    constant.MAX_DEPTH = 2
    WebCrawler.queue_link.add(constant.HOMEPAGE_URL)
    WebCrawler(constant.HOMEPAGE_URL)
  
    depth = 1
    print(type(constant.MAX_DEPTH))
    print(depth)
    print(float(constant.MAX_DEPTH))
    while( (WebCrawler.queue_link and depth < constant.MAX_DEPTH ) and len(WebCrawler.crawled_link) < 20):
        #url = WebCrawler.queue_link.pop()
        #WebCrawler.queue_link.add(url)
       
        print(len(WebCrawler.crawled_link))
        url = next(iter(WebCrawler.queue_link))
        if (url not in WebCrawler.crawled_link ):
            WebCrawler(url)
        #crawl(WebCrawler.queue_link.pop())
        #if(len(WebCrawler.crawled_link) > 10):
        if not WebCrawler.queue_link:
            WebCrawler.queue_link, WebCrawler.next_links =  WebCrawler.next_links, set()

            depth += 1
    print("Time taken to execute : " + str(time.time() - t))

def create_threads():

    t = time.time()

    threads_list = [0] * constant.NUMBER_OF_THREADS
    for i in range(constant.NUMBER_OF_THREADS):
        threads_list[i] = threading.Thread(target=search_web)
        #threads_list[i].daemon = True
        threads_list[i].start()
    for i in range(constant.NUMBER_OF_THREADS):
        threads_list[i].join()
    

    print("Time taken to execute : " + str(time.time() - t))


def crawl_web_page():
    create_threads()
    #search_web()


