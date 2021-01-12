""" Producer Views """

# Django Rest Framework
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Models
from producer.models import(
    Pollster,
    Producer,
    ProducerHome,
    ProducerPerson
    )

# Django
from django.db.models import Prefetch

# Serializers
from producer.serializers import PollsterSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

class PollsterViewSet(viewsets.ModelViewSet):
    queryset = Pollster.objects.all()
    serializer_class = PollsterSerializer
    pagination_class = StandardResultsSetPagination
    #permission_classes = (IsAuthenticated, )
        # Filters
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('producer')

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(PollsterViewSet, self).get_serializer(*args, **kwargs)

class ProductiveDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pollster.objects.all()
    serializer_class = PollsterSerializer

'''
    def perform_create(self, serializer):
        """Assign circle admin."""
        user = self.request.user
        profile = user.profile
        pollster = serializer.save()
        print(user)

class ProducerListViewset(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerListSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated, )
    
    # Filters
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('last_name', 'first_name', 'document')


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(
                Prefetch('productions')
            )
        return queryset

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(
                Prefetch('productions')
            )
        return queryset

    def get_queryset(self):
        params = self.request.query_params.get(
            'id',
            ''
        )
        return Producer.objects.filter(
            last_name__icontains = params
        )


class CreateProduction(generics.ListCreateAPIView):
    serializer_class = ProductionSerializer

    def get_queryset(self):
        """
        This view should return a list filter of the location for
        the user as determined by the username portion of the URL.
        """
        producer = self.kwargs['producer']
        return Production.objects.filter(producer=producer)
'''