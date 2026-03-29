from rest_framework import serializers

from ad.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'description', 'phone_number', 'is_premium', 'date_created']
