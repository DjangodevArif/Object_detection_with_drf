from rest_framework.decorators import api_view, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import FileResponse
from .serializers import DetectImageSer
from PIL import Image
from io import BytesIO
import uuid
from ultralytics import YOLO
import cv2
import numpy as np


@api_view()
@renderer_classes([JSONRenderer])
def index(request):
    return Response("Hello, world. You're at the main page",)


class DetectImage(APIView):
    serializer_class = DetectImageSer
    permission_classes = [AllowAny]

    def post(self, request):
        serialize = DetectImageSer(data=request.data)
        if serialize.is_valid(raise_exception=True):
            data = serialize.validated_data.get("file")
            unique = str(uuid.uuid4()).split("-")[0]
            # image = Image.open(BytesIO(data.file.read()))
            image_array = np.frombuffer(data.file.read(), np.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            model = YOLO('yolov8n.pt')
            file_name = "result_" + unique
            results = model(image, save=True,
                            project="detect", name=file_name)
            detect_image = "detect/"+file_name+"/image0.jpg"
        # return Response(image, content_type="image/jpg")
        return FileResponse(open(detect_image, "rb"), as_attachment=False)
