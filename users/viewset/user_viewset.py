from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models.user_models import UserModels
from users.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModels.objects.all()


# Surcharge de la methode create pour crypter le mot de passe a la création
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if 'password' in data:
            data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return JsonResponse(serializer.data, status=201)

    @action(detail=False, methods=['post'], url_path='change-password', url_name='change_password')
    def change_password(self, request, *args, **kwargs):
        user = request.user
        data = request.data


        current_password = data.get('old')
        new_password = data.get('new')


        if not user.check_password(current_password):
            return Response({"error": "Current password is incorrect."}, status=400)


        if not new_password:
            return Response({"error": "New password must be provided."}, status=400)


        user.password = make_password(new_password)
        user.save()

        return Response({"message": "Password changed successfully."}, status=200)
