from django.urls import path,include
from . import views  # Import your views module




urlpatterns = [

    path('', views.add_visitor, name='add-visitor'),
    path('enter-unique-id/', views.enter_unique_id, name='enter-unique-id'),
    #path('feedback/', views.feedback, name='feedback'),

    path('save-captured-photo/', views.save_captured_photo, name='save-captured-photo'),
    path('receipt/', views.visitor_receipt, name="visitor-receipt"),
    path('dashboard/', views.visitors, name='visitors'),
    path('provide-feedback/<int:visitor_id>/', views.provide_feedback, name='provide-feedback'),
]

