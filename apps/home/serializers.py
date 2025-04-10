from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

    def validate_role(self, value):
        """Prevent non-admins from modifying roles."""
        if self.context["request"].user.is_admin:
            return value
        raise serializers.ValidationError("Only admins can assign roles.")
