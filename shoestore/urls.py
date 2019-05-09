from django.urls import path, include
from . import views
# routers takes care off generating all the urls for the particular model
# ex: GET request on '/manufacturer' would return all manufacturers
# POST request on '/manufacturer/' would create a new manufacturer
# '/manufacturer/1' gets first manufacturer in db
from rest_framework import routers


router = routers.DefaultRouter()
router.register('manufacturer', views.ManufacturerView)
router.register('shoetype', views.ShoeTypeView)
router.register('shoecolor', views.ShoeColorView)
router.register('shoe', views.ShoeView)

# router.urls auto-generates the urls for the path
# creates nice html view
urlpatterns = [
    path('', include(router.urls))
]
