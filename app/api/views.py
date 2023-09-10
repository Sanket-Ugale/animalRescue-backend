from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from app.models import Item
from app.api.serializers import ItemSerializer


@api_view(["GET"])
def api_detail_item_view(request, slug):
    try:
        item = Item.objects.get(slug=slug)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    


# @api_view(["PUT"])
# def api_update_item_view(request, slug):
#     try:
#         item = Item.objects.get(slug=slug)
#     except Item.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'PUT':
#         serializer = ItemSerializer(item, data=request.data)
#         data={}
#         if serializer.is_valid():


#         return Response(serializer.data)
    