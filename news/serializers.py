from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.main_image = validated_data.get('main_image', instance.main_image)
        instance.preview_image = validated_data.get('preview_image', instance.preview_image)
        instance.text = validated_data.get('text', instance.text)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
