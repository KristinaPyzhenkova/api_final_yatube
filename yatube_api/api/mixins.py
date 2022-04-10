from rest_framework import viewsets
from rest_framework import mixins


class GetViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    pass
