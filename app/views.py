import json
from rest_framework import viewsets, generics

from app.serializers import InjuryPredictSerializer
from .models import Item
from app.api.serializers import ItemSerializer
# from tensorflow.keras.models import load_model
from django.views.decorators.csrf import csrf_exempt
# import pickle
from django.shortcuts import render
from rest_framework import status
# Create your views here.
from django.shortcuts import render
from keras.preprocessing import image
from joblib import load
import numpy as np
from PIL import Image
from rest_framework.renderers import JSONRenderer
from app.serializers import InjuryPredictSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import tensorflow as tf
from rest_framework.decorators import api_view, renderer_classes


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@csrf_exempt
@api_view(['POST'])
@renderer_classes([JSONRenderer])
def InjuryPredict(request):
    if request.method == 'POST':
        # Load the .h5 model file
        model_path = 'app/models/imageClassifier.h5'
        model = tf.keras.models.load_model(model_path)
        
        # Check if the request has form data
        if request.FILES.get("AnimalImage"):
            animal_image = request.FILES.get("AnimalImage")
            # Read the image data and resize it to match the expected input shape of the model
            pil_image = Image.open(animal_image)
            pil_image = pil_image.convert('RGB')  # Ensure the image is in RGB format
            pil_image = pil_image.resize((256, 256))  # Resize the image to (180, 180)
            
            # Convert the resized image to a NumPy array
            x = image.img_to_array(pil_image)
            test_img = np.expand_dims(x, axis=0)
            
            result = model.predict(test_img)
            # print("++++++++++++++++++++++++ "+str(result))  
            output=""  
            if result[0]<0.5:
                output="hurt"        
            else:
                output="not hurt"
            return Response({"Result": output})
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)