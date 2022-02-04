
from rest_framework.viewsets import ModelViewSet
from .models import Newsletter
from .serializers import NewsletterSerializer, CreateNewsletterSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .permissions import CustomPermission
from django.core.mail import send_mail


class NewsletterViewSet(ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return CreateNewsletterSerializer
        return NewsletterSerializer

    # creacion de filtro a través de los parametros de la url
    def get_queryset(self):
        filter = self.request.query_params.get('tag')
        if filter:
            # este queryset es el del comienzo de la clase
            newsletter = self.queryset.filter(
                tags__slug__contains=filter
            )
            return newsletter
        return self.queryset  # este queryset es el del comienzo de la clase

    @action(methods=['PATCH'], detail=True, permission_classes=[CustomPermission])
    def votes(self, request, pk=None):
        user = request.user
        id = user.id
        newsletter = self.get_object()
        votes = newsletter.voters.all()
        if user in votes:
            newsletter.voters.remove(id)
            return Response(status=status.HTTP_200_OK,
                            data={
                                "vote": "Vote Removed"
                            })
        newsletter.voters.add(id)
        return Response(status=status.HTTP_200_OK,
                        data={
                            "vote": "Vote Added"
                        })

    @action(methods=['PATCH'], detail=True, permission_classes=[CustomPermission])
    def subscribe(self, request, pk=None):
        user = request.user
        id = user.id
        newsletter = self.get_object()
        subscribers = newsletter.subscribers.all()
        if newsletter.target <= len(newsletter.voters.all()):
            if user in subscribers:
                newsletter.subscribers.remove(id)
                return Response(status=status.HTTP_200_OK,
                                data={"suscribe": "Suscritor Removed"})
            newsletter.subscribers.add(id)
            return Response(status=status.HTTP_200_OK,
                            data={"suscribe": "Suscritor Added"})
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                        data={"Error": "Theres not enough votes to get subscribe"})

    @action(methods=['POST'], detail=True,)
    def invitation(self, request, pk=None):
        user_staff = request.user.is_staff
        user = request.user
        newsletter = self.get_object()
        print(user.email)

        if user_staff:
            send_mail(
                'Invitation to Subscribe',
                'Hi!, I invite you to subscribe to this Newsletter!',
                f'{user.email}',
                [f'example@example.com'],
                fail_silently=False,
            )
            return Response(status=status.HTTP_200_OK,
                 data={"Invitation send it"})

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                 data={"Not Allow to send an invitation"})

