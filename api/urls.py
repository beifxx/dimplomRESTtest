from django.contrib import admin
from django.urls import path

from api import views
from api.views import *

urlpatterns = [
    path('products', ProductAPIView.as_view()),
    path('products/<int:pk>', ProductDetailsAPIView.as_view()),

    path('news', PromoAPIView.as_view()),
    path('news/<int:pk>', PromoDetailsAPIView.as_view()),

    path('support_requests', SupportRequestAPIView.as_view()),
    path('support_requests/<int:pk>', SupportRequestDetailsAPIView.as_view()),

    path('interest_rates', InterestRateAPIView.as_view()),
    path('interest_rates/<int:pk>', InterestRateDetailsAPIView.as_view()),

    path('client_profiles', ClientProfileAPIView.as_view()),
    path('client_profiles/<int:pk>', ClientProfileDetailsAPIView.as_view()),

    path('applications', ApplicationAPIView.as_view()),
    path('applications/<int:pk>', ApplicationDetailsAPIView.as_view()),

    path('deals', DealAPIView.as_view()),
    path('deals/<int:pk>', DealDetailsAPIView.as_view()),

    path('documents', DocumentAPIView.as_view()),
    path('documents/<int:pk>', DocumentDetailsAPIView.as_view()),
    path('client_documents/<int:client_id>', DocumentToClientAPIView.as_view())
]
