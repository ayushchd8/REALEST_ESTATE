from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realtors
from .serializers import RealtorSerializers

class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realtors.objects.all()
    serializer_class = RealtorSerializers
    pagination_class = None

class RealtorView(RetrieveAPIView):
    queryset = Realtors.objects.all()
    serializer_class = RealtorSerializers
    
class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realtors.objects.filter(top_seller=True)
    serializer_class = RealtorSerializers
    pagination_class = None