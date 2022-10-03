import sys
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
        set_keys = set(request.data.keys())
        model_dict = {'title': str, 'module': str, 'description': str, 'students': int, 'is_active': bool}
        set_fields = set(model_dict.keys())
        diff = set_fields - set_keys
        dict = {}
        if len(diff) > 0:
            for i in diff:
                dict[i] = "missing key"
            return Response(dict, status=status.HTTP_400_BAD_REQUEST)
        else:
            for key in set_fields:
                if type(request.data[key]) != model_dict[key]:
                    dict[key] = f'Must be {model_dict[key].__name__}'
            if len(dict) > 0:
                return Response(dict, status=status.HTTP_400_BAD_REQUEST)
            else:
                content = Content.objects.create(**request.data)
                return Response(model_to_dict(content), status=status.HTTP_201_CREATED)

class ContentDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        try:
            content = Content.objects.get(id=pk)
            return Response(model_to_dict(content), status=status.HTTP_200_OK)
        except Content.DoesNotExist:
            return Response({'error': 'Content not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request: Request, pk: int) -> Response:
        try:
            content = Content.objects.get(id=pk)
        except Content.DoesNotExist:
            return Response({'error': 'Content not found'}, status=status.HTTP_404_NOT_FOUND)
        for key, value in request.data.items():
            setattr(content, key, value)
        content.save()
        content_dict = model_to_dict(content)
        return Response(content_dict, status=status.HTTP_200_OK)
        
    def delete(self, request: Request, pk: int) -> Response:
        try:
            content = Content.objects.get(id=pk)
        except Content.DoesNotExist:
            return Response({'error': 'Content not found'}, status=status.HTTP_404_NOT_FOUND)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

               
       

                 
                

           

        
      

