from rest_framework import serializers
from .models import CustomUser, Task, Team

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'email', 'phone', 'role', 'date_joined', 'password', 'password2')
        #extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def create(self, validated_data):
        user = CustomUser(name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            role=validated_data['role'],
            password=validated_data['password'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'team', 'status', 'started_at', 'completed_at']

    


class TeamSerializer(serializers.ModelSerializer):
    Task = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['name', 'team_leader', 'team_membars', 'Task']


