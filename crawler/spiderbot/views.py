from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from spiderbot.view_models import AssignmentMainResponse, WebPageDataResponse
from spiderbot.serializer_view_models import WebPageDataMainSerializer
from .models import WebImage, WebPage
# Create your views here.

from .web_crawler import WebCrawler
import spiderbot.constant as constant
import threading
import time

def search_web(seed_url, depth):
    """
    It searches the web page for all the urls in the home and goes in depth of the crawled urls.

    """
    t = time.time()
    constant.HOMEPAGE_URL = seed_url
    constant.MAX_DEPTH = 2
    WebCrawler.queue_link.add(constant.HOMEPAGE_URL)
    WebCrawler(constant.HOMEPAGE_URL)
   
    depth = 1
    
    while( (WebCrawler.queue_link and depth < constant.MAX_DEPTH ) and len(WebCrawler.crawled_link) < 5):
       
        url = next(iter(WebCrawler.queue_link))
        if (url not in WebCrawler.crawled_link ):
            WebCrawler(url)
        
        if not WebCrawler.queue_link:
            WebCrawler.queue_link, WebCrawler.next_links =  WebCrawler.next_links, set()

            depth += 1
    print("Time taken to execute : " + str(time.time() - t))

def create_threads(seed_url, depth):

    t = time.time()

    threads_list = [0] * constant.NUMBER_OF_THREADS
    for i in range(constant.NUMBER_OF_THREADS):
        threads_list[i] = threading.Thread(target=search_web, args=(seed_url, depth))
        #threads_list[i].daemon = True
        threads_list[i].start()
    for i in range(constant.NUMBER_OF_THREADS):
        threads_list[i].join()
    

    print("Time taken to execute : " + str(time.time() - t))


@api_view(['POST'])
def crawl_web_page(request):
    request_data = JSONParser().parse(request)
    seed_url = request_data['seed_url']
    depth = request_data['depth']

    WebCrawler.queue_link = set()
    WebCrawler.crawled_link = set()

    WebCrawler.queue_image = set()
    WebCrawler.crawled_image = set()

    create_threads(seed_url, depth)


    try:
        
        web_page_objs_list = []
       
        for web_link in list(WebCrawler.crawled_link):
            web_page_objs_list.append(WebPage.objects.filter(crawled_url  = web_link).order_by('-created_at').first())

    except ObjectDoesNotExist:
        web_page_objs_list = None

    main_response = AssignmentMainResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = WebPageDataResponse(web_page_objs_list)
   
    serializer = WebPageDataMainSerializer(main_response)

    return Response(serializer.data)







