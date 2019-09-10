from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins


class GeneralObjectByMultiParamsForRetrieveAndUpdate(mixins.RetrieveModelMixin,
                                                     mixins.UpdateModelMixin,
                                                     generics.GenericAPIView,):
    """
    General methods for API for objects details showing and updating by searching special keywords.
    """
    def __init__(self, serializer_class, basemodel_class, *args, **kwargs):
        self.serializer_class = serializer_class
        self.basemodel_class = basemodel_class
        self.args = args
        self.kwargs = kwargs

    def get_object_by_one_parm(self, key, value):
        try:
            self.basemodel_class.objects.objects.all(key=value)
        except self.basemodel_class.DoesNotExist:
            raise Http404

