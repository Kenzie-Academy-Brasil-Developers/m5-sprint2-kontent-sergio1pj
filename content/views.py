from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
from .models import Content


class ContentView(APIView):
    def get(self, request: Request) -> Response:
        contents = Content.objects.all()
        content_list = []
        for content in contents:
            content_list.append(model_to_dict(content))
        return Response(content_list, status=status.HTTP_200_OK)
       
    def post(self, request: Request) -> Response:
        for key, value in request.data.items():
            if not value:
                return Response({'error': f'{key} is missing'}, status=status.HTTP_400_BAD_REQUEST)
        content = Content.objects.create(**request.data)
        return Response(model_to_dict(content), status=status.HTTP_201_CREATED)
