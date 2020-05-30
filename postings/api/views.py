from rest_framework import generics
from postings.models import myAdmin
from .serializers import myAdminSerializer

class myAdminRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = myAdminSerializer
    # queryset = myAdmin.objects.all()

    def get_queryset(self):
        return myAdmin.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return myAdmin.objects.all()