from rest_framework import views, status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ad.models import Ad
from users.models import CustomUser
from users.serializers import RegisterUserSerializer, LoginUserSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


class UserLoginAPIView(GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = CustomUser.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"detail": "Invalid credentials"}, status=400)


class SubscriptionView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        premium_ads = Ad.objects.filter(owner=user)
        user.subscription = not user.subscription
        for ad in premium_ads:
            ad.is_premium = user.subscription
            ad.save()
        user.save()
        return Response({'subscription': user.subscription}, status=status.HTTP_200_OK)


