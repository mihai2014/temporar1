from rest_framework import serializers
from notes.models import Notes

class NotesSerializer0(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    content = serializers.CharField(required = True, max_length=50, allow_blank=True)

    def create(self, validated_data):
        """
        Create and return a new `Notes` instance, given the validated data.
        """
        print("create0")
        return Notes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Notes` instance, given the validated data.
        """
        print("update0")
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class NotesSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'content']

    # customize

    def create(self, validated_data):
        """
        Create and return a new `Notes` instance, given the validated data.
        """
        print("create1")
        return Notes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Notes` instance, given the validated data.
        """
        print("update1")
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance        


    

