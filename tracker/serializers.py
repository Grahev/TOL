from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'job_no',
            'job_type',
            'customer_order_ref',
            'order_date',
            'process_date',
            'order_value',
            'customer',
            'account_type',
            'project_engineer',
            'status',
            'doors_s',
            'doors_d',
            'order_req_by_date',
            'handling_floor_plans',
            'comments',
            'date_sent_for_approval',
            'date_approval_recived',
            'date_into_production',
            'date_dispatch',
        )
