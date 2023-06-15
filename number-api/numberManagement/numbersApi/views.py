from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import requests

class NumbersAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        urls = request.GET.getlist('url')
        numbers = set()

        for url in urls:
            try:
                response = requests.get(url, timeout=0.5)
                if response.status_code == 200:
                    data = response.json()
                    numbers.update(data.get('numbers', []))
            except requests.exceptions.Timeout:
                pass

        sorted_numbers = sorted(numbers)
        return Response({'numbers': sorted_numbers}, status=status.HTTP_200_OK)