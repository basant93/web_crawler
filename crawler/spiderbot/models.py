from django.db import models

# Create your models here.


class WebPage(models.Model):

    crawled_url = models.CharField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.crawled_url


class WebImage(models.Model):

    image_url = models.CharField(max_length=2000, blank=True, null=True)
    web_page = models.ForeignKey(WebPage, max_length=2000, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.image_url