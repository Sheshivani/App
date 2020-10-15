from django.db.models import Q
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Spam
from .serializer import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def search_user(request):
    data = request.data
    search = data["search"]
    # import ipdb; ipdb.set_trace()
    if search:
        users = User.objects.filter(
            Q(first_name__icontains=search) | Q(phone__icontains=search) | Q(username__icontains=search) | Q(email__icontains=search))
        serializer = UserSerializer(users, many=True)
    if serializer.data:
        return Response(serializer.data, status=404)
    return Response(serializer.data, status=200)


class UserRegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(self):
            serializer.save()
            return JsonResponse({'result': 'success', 'message': 'User created Successfully'})
        return JsonResponse({'result': 'error', 'message': 'Failed!!'})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def mark_spam(request):
    data = request.data
    phone = data["phone"]
    if phone:
        spam_user = Spam.objects.create(phone=phone, by_id=request.user.id)
        return Response({"message": "marked spam successfully"}, status=200)
    return Response({"message": "some error occurred"}, status=401)



