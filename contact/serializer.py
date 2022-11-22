from .models import Info , Portfolio , ProfileImage , Skill
from rest_framework import serializers


class InfoSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Info
        fields = '__all__'
        
class PortfolioSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Portfolio
        fields = '__all__'

class ProfileImageSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = ProfileImage
        fields = '__all__'

class SkillSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = '__all__'
