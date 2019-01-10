from rest_framework import serializers

class WebImageResponse(serializers.Serializer):
    image_url = serializers.CharField()



class ImageDataSerializer(serializers.Serializer):
    web_url =serializers.CharField()
    web_image_urls = WebImageResponse(many=True)



class WebPageDataSerializer(serializers.Serializer):
    image_urls = ImageDataSerializer(many=True)


class WebPageDataMainSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    error_code = serializers.IntegerField()
    status_code = serializers.CharField()
    data = WebPageDataSerializer()