# This is my first django REST framework

## I have built a simple shoestore API contained in the project I named 'djangorest' that can do http requests using a serializer that translates json data.

### djangorest/settings.py

1. Interacting with these apps:
   'rest_framework',
   'djangorest',
   'shoestore'

### shoestore/serializers.py

1. I used 'serializers.ModelSerializer' that allows me to target all data or grab specific data if needed.
2. subclass I named Meta which points to the model and all the fields the ModelSerializer is going to use

### shoestore/urls.py

1. Using routers.DefaultRouter() imported from rest_framework which allows automatic URL routing to Django after registering the url prefix and viewset class it is pointing to
   **Note:** The project urls.py ('djangorest/urls.py') file points to the API urls.py

### shoestore/views.py

1. Using viewsets.ModelViewSet imported from rest_framework which **generalizes** the request handling instead of having to define each type of request.
2. Major benefit in reducing the amount of code, due to _somewhat_ pre-standardized methods in a REST API (GET, PUT, POST, etc.)
3. Using viewsets.ModelViewSet allows us to only have to worry about how to get objects from the database
   1. I have created a queryset object containing all of the model objects and specified the serializer that will translate JSON.
