from django.shortcuts import render
from django.views import View

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import CategorySerializer, VideoSerializer
from main.models import Category, Video


class BaseAPIView(View):
    """ API navigations """

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        videos = Video.objects.filter(blocked=False, private=False)
        context = {'categories': categories, 'videos': videos}
        return render(request, 'api/base_api.html', context)


class Pagination(PageNumberPagination):
    """ Pagination """

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class CategoryListAPIView(ListAPIView):
    """ List category """

    serializer_class = CategorySerializer
    pagination_class = Pagination
    queryset = Category.objects.all()


class VideoListAPIView(ListAPIView):
    """ List videos """

    serializer_class = VideoSerializer
    pagination_class = Pagination
    queryset = Video.objects.filter(blocked=False, private=False)


class CategoryDetailAPIView(RetrieveAPIView):
    """ Category Detail """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'


class VideoDetailAPIView(RetrieveAPIView):
    """ Video Detail """

    serializer_class = VideoSerializer
    queryset = Video.objects.filter(blocked=False, private=False)
    lookup_field = 'id'
