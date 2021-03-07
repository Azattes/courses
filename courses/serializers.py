from rest_framework import serializers
from courses.models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'imgpath')

class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'value')

class CourseSerializers(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
    contacts = ContactSerializers(many=False)
    branches = BranchSerializers(many=False)


    class Meta:
        model = Course
        fields = ('name', 'description', 'logo', 'category', 'contacts', 'branches')

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')

        instance.name = validated_data.get(
            'name', 
            instance.name
        )
        instance.description = validated_data.get(
            'description',
            instance.description
        )
        instance.logo = validated_data.get(
            'logo',
            instance.logo
        )
        instance.category = validated_data.get(
            'category',
            instance.category
        )
        instance.contacts = validated_data.get(
            'contacts',
            instance.contacts
        )
        instance.branches = validated_data.get(
            'branches',
            instance.branches
        )
        instance.save()
        return instance
