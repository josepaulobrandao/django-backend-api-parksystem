from rest_framework import generics
from rest_framework.response import Response
from app.models import Person
from app.serializer import PersonSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class AllPersonListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer   

class PresonUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    partial = True
class PersonDeleteView(generics.DestroyAPIView): 
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.delete()
            return Response(print("delete Person"))
        
# https://medium.com/@learncodeguide/creating-a-crud-api-with-django-rest-framework-and-postgresql-3ead7ffb140f