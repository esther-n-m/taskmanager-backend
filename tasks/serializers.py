from rest_framework import serializers
from .models import Task
from django.utils import timezone
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at', 'completed_at')

    def validate_due_date(self, value):
        # Due date must be today or future
        if value and value < date.today():
            raise serializers.ValidationError("Due date must be today or in the future.")
        return value

    def update(self, instance, validated_data):
        """
        - If task is Completed (status='C'), you cannot edit anything
          unless you are reverting status from 'C'.
        - When moving to 'C', set completed_at = now.
        - When moving away from 'C', clear completed_at.
        """
        incoming_status = validated_data.get('status', instance.status)

        # If currently completed and staying completed, block any other edits
        if instance.status == 'C' and incoming_status == 'C':
            non_status_fields = [k for k in validated_data.keys() if k != 'status']
            if non_status_fields:
                raise serializers.ValidationError(
                    "Completed tasks cannot be edited. Mark as incomplete first."
                )

        # Handle completed_at transitions
        if instance.status != 'C' and incoming_status == 'C':
            validated_data['completed_at'] = timezone.now()
        if instance.status == 'C' and incoming_status != 'C':
            validated_data['completed_at'] = None

        return super().update(instance, validated_data)