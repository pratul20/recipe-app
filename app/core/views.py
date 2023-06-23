"""
Core views for app
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def health_check(request):
    """Returns successful response"""
    return Response({'healthy': True}, status=status.HTTP_200_OK)
