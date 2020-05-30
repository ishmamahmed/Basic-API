from rest_framework import serializers
from postings.models import myAdmin

class myAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = myAdmin
        fields = [
            'pk',
            'user',
            'name',
            'email',
            'description',
        ]