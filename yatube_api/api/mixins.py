from rest_framework import viewsets, mixins


class GetViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    pass
