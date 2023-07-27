from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, TemperatureMeasurementSerializer


class SensorListCreateView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)
            serializer = SensorSerializer(sensor)
            return Response(serializer.data)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)
            serializer = SensorSerializer(sensor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)
            sensor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TemperatureMeasurementCreateView(APIView):
    def get(self, request):
        measurements = TemperatureMeasurement.objects.all()
        serializer = TemperatureMeasurementSerializer(measurements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TemperatureMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
