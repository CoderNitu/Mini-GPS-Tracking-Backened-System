from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from .models import Device, LocationData
from .serializers import DeviceSerializer, LocationDataSerializer
from .throttles import DeviceThrottle
from .utils import haversine_distance

# Register Device (Public)
class RegisterDeviceView(APIView):
    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            device = serializer.save()
            return Response(DeviceSerializer(device).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Submit GPS Location (Authenticated)

class SubmitLocationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [DeviceThrottle] 

    def post(self, request):
        serializer = LocationDataSerializer(data=request.data)
        if serializer.is_valid():
            device_id = serializer.validated_data['device'].device_id
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']

            # Get previous location
            previous = LocationData.objects.filter(device__device_id=device_id).order_by('-timestamp').first()
            distance = None

            if previous:
                distance = haversine_distance(
                    previous.latitude, previous.longitude,
                    latitude, longitude
                )

            location = serializer.save()

            response_data = LocationDataSerializer(location).data
            response_data['distance_from_previous'] = round(distance, 3) if distance else 0.0

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Location History (Authenticated)
from rest_framework.pagination import PageNumberPagination

class LocationHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, device_id):
        try:
            device = Device.objects.get(device_id=device_id)
        except Device.DoesNotExist:
            return Response({'error': 'Device not found'}, status=404)

        data = LocationData.objects.filter(device=device)

        # Optional filters
        start = request.query_params.get('start_time')
        end = request.query_params.get('end_time')
        latest = request.query_params.get('latest')

        if start:
            data = data.filter(timestamp__gte=start)
        if end:
            data = data.filter(timestamp__lte=end)
        if latest == 'true':
            data = data.order_by('-timestamp')[:1]
            serializer = LocationDataSerializer(data, many=True)
            return Response(serializer.data)

        # Apply pagination
        paginator = PageNumberPagination()
        paginated_data = paginator.paginate_queryset(data.order_by('-timestamp'), request)
        serializer = LocationDataSerializer(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)
    
from rest_framework.generics import ListAPIView

class DeviceListView(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

