from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewsThree
from .serializers import NewsThreeSrializers


class NewsThreeList(APIView):
    def get(self, request):
        queryset = NewsThree.objects.all()
        serializer = NewsThreeSrializers(queryset, many=True)
        return Response({'news': serializer.data})
