from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
# from .view_model import StudentProfileResponse, StudentProfileDataResponse
# from .serializer_view_models import StudentProfileMainSerializer
from spiderbot.view_models import AssignmentMainResponse, WebPageDataResponse
from spiderbot.serializer_view_models import WebPageDataMainSerializer
from .models import WebImage, WebPage
# Create your views here.

from .web_crawler import WebCrawler
import spiderbot.constant as constant
import threading
import time

def search_web(seed_url, depth):
    t = time.time()
    constant.HOMEPAGE_URL = seed_url
    constant.MAX_DEPTH = 2
    WebCrawler.queue_link.add(constant.HOMEPAGE_URL)
    WebCrawler(constant.HOMEPAGE_URL)
  
    depth = 1
    print(type(constant.MAX_DEPTH))
    print(depth)
    print(float(constant.MAX_DEPTH))
    while( (WebCrawler.queue_link and depth < constant.MAX_DEPTH ) and len(WebCrawler.crawled_link) < 5):
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

    create_threads(seed_url, depth)

    #search_web()

    try:
        # If exception is not thrown, username already exists.
        web_page_objs = WebPage.objects.filter(crawled_url__in = list(WebCrawler.crawled_link))
    except ObjectDoesNotExist:
        web_page_objs = None

    main_response = AssignmentMainResponse()
    main_response.success = True
    main_response.error_code = 0
    main_response.status_code = status.HTTP_200_OK
    main_response.data = WebPageDataResponse(web_page_objs)
    serializer = WebPageDataMainSerializer(main_response)

    return Response(serializer.data)







