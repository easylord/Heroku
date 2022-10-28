from rest_framework import serializers
from .models import Stores
from authentication.serializers import RegisterSerializer
from authentication.models import User

class StoreSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())

    profile_image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)

    class Meta:
        model = Stores
        #fields = ['id','name', 'adress', 'description', 'owner', 'profile_image', 'delivery']
        fields = "__all__"
        #extra_kwargs = {'password': {'write_only': True}}
        
    # def create(self, validated_data):
    #     owner_data = validated_data.pop('owner')
    #     stores = Stores.objects.create(**validated_data)
    #     for owner_data in owner_data:
    #         User.objects.create(owner=stores, **owner_data)
    #     return stores

    def update(self, instance, validated_data):
        owner_data = validated_data.pop('owner')
        stores = (instance.owner).all()
        stores = list(stores) 
        instance.name = validated_data.get('name', instance.name)
        instance.adress = validated_data.get('adress', instance.adress)
        instance.description = validated_data.get('description', instance.description)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.delivery = validated_data.get('delivery', instance.delivery)

        for owner_data in owner_data:
            store = stores.pop(0)
            store.username = owner_data.get('username', store.username)
            store.save()

        return instance

        #return super().create(validated_data)