from rest_framework import serializers

from vehicle.models import Car, Moto, Milage
from vehicle.validators import TitleValidator


class MilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = '__all__'


# Задача 1
class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage', read_only=True) # Задача 4
    milage = MilageSerializer(many=True, read_only=True)  # Задача 5

    class Meta:
        model = Car
        fields = '__all__'


# Задача 2
class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField() # Задача 4

    class Meta:
        model = Moto
        fields = '__all__'

    # Задача 4
    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().milage
        return 0

    # # можно записать так:
    # @staticmethod
    # def get_last_milage(instance):
    #     if instance.milage_set.all().first():
    #         return instance.milage_set.all().first().milage
    #     return 0


# Задача 3
class MilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = '__all__'


# Задача 5
class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto',)


# Задача 6
class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'
        #11.2
        validators = [
            TitleValidator(field='title'),
            # 11.3 Валидатор на уникальность(чтобы пользователь не мог внести тот же самый продукт с тем же самым годом выпуска)
            serializers.UniqueTogetherValidator(fields=['title', 'description'], queryset=Moto.objects.all())
        ]

    def create(self, validated_data):
        milage = validated_data.pop('milage')# берем из validated_data и исключаем по ключу 'milage'

        moto_item = Moto.objects.create(**validated_data)

        for m in milage:
            Milage.objects.create(**m, moto=moto_item) #создается новый пробег

        return moto_item