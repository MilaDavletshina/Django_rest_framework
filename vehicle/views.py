from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from vehicle.models import Car, Moto, Milage
from vehicle.paginators import VehiclePaginator
from vehicle.permissions import IsOwnerOrStaff
from vehicle.serliazers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, \
    MotoCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# Задача 1
class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer #созданный ранее серилизатор
    queryset = Car.objects.all() #для вывода активных/неактивных элементов, для работы с пользователя одного кода типа

    #9.5
    permission_classes = [AllowAny] #11.6 IsAuthenticated изменено на AllowAny


# Задача 2
class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer # изменено в Задаче 6 с MotoSerializer
    permission_classes = [IsAuthenticated] #10.3


    #10.3
    def perform_create(self, serializer):
        """сохраняем владельца"""
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()

    # #можно использовать вместо замены MotoSerializer на MotoCreateSerializer, в этом случае serializer_class = MotoSerializer
    # def post(self, *args, **kwargs):
    #     self.serializer_class = MotoCreateSerializer
    # super()


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    #11.4
    pagination_class = VehiclePaginator


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView): #поддерживает и put и patch
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()

    # 10.4
    permission_classes = [IsOwnerOrStaff] #из permissins.py


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


# Задача 3
class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer


# Задача 7
class MilageListAPIView(generics.ListAPIView):
    serializer_class = MotoMilageSerializer
    queryset = Milage.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto')
    ordering_fields = ('year',)


# Задача 5
class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer


