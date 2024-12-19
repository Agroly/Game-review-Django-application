from django.http import Http404
from django.utils.timezone import now
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import User
from .serializers import UserRegistrationSerializer, CustomTokenObtainPairSerializer, \
    UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED
        )


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            user.last_login = now()
            user.save()

        return response


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def get_object(self):
        user_id = self.kwargs.get('id')
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404


class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Profile updated successfully',
            'data': UserProfileSerializer(self.get_object()).data
        }, status=status.HTTP_200_OK)


class RoleUpdateView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        new_role = request.data.get('role')
        if new_role not in ['user', 'moderator', 'admin']:
            return Response(
                {"detail": "Invalid role."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if user == request.user:
            return Response(
                {"detail": "You cannot change your own role."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.role = new_role
        if new_role == 'admin':
            user.is_staff = True
        else:
            user.is_staff = False
        user.save()

        return Response(
            {
                "message": f"User's role updated to {new_role}",
                "data": UserProfileSerializer(user).data
            },
            status=status.HTTP_200_OK
        )


class UserDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if user == request.user:
            return Response(
                {"detail": "You cannot delete your own account."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().delete(request, *args, **kwargs)

