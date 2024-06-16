from rest_framework import serializers

from main.models import House, HouseType, HousePlanPhoto, HouseFacadePhoto, HouseSectionPhoto, HousePhoto, ImprovementPhoto, \
    SignUpForAFreeConsultation, CallBack, Improvement


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = ["id", "name", "room", "floor", "bathroom", "square",
                  "building_materials_equipment", "cost_of_basic_equipment", "main_photo"]


class HouseTypeSerializer(serializers.ModelSerializer):
    house_set = HouseSerializer(many=True)

    class Meta:
        model = HouseType
        fields = ["material", "house_set"]


class HousePlanPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = HousePlanPhoto
        fields = '__all__'


class HouseFacadePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseFacadePhoto
        fields = '__all__'


class HouseSectionPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseSectionPhoto
        fields = '__all__'


class HousePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePhoto
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseType
        fields = ["material"]


class HouseAllSerializer(serializers.ModelSerializer):
    houseplanphoto_set = HousePlanPhotoSerializer(many=True)
    housefacadephoto_set = HouseFacadePhotoSerializer(many=True)
    housesectionphoto_set = HouseSectionPhotoSerializer(many=True)
    housephoto_set = HousePhotoSerializer(many=True)
    material = MaterialSerializer()

    class Meta:
        model = House
        fields = ["id", "name", "room", "floor", "bathroom", "square", "facade",
                  "description", "material", "main_photo", "cost_of_basic_equipment",
                  "building_materials_equipment", "link_to_video_on_youtube",
                  "houseplanphoto_set", "housefacadephoto_set", "housesectionphoto_set",
                  "housephoto_set"]


class ConsultationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SignUpForAFreeConsultation
        fields = ["name", "phone_number", "date_of_consultation"]


class CallBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallBack
        fields = ["name", "phone_number"]


class ImprovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Improvement
        fields = "__all__"


class ImprovementPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImprovementPhoto
        fields = "__all__"
        


class ImprovementDetailSerializer(serializers.ModelSerializer):
    improvementphoto_set = ImprovementPhotoSerializer(many=True)

    class Meta:
        model = Improvement
        fields = "__all__"