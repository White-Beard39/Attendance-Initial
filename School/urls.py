from django.contrib import admin
from django.urls import path, include
from School.views import SchoolViewSet, BranchViewSet, TeacherViewSet, StudentViewSet, ParentViewSet, ClassesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 

router.register(r'schools', SchoolViewSet)  # Register the viewset
router.register(r'branch', BranchViewSet)  # Register the viewset
router.register(r'teacher', TeacherViewSet)  # Register the viewset
router.register(r'student', StudentViewSet)  # Register the viewset
router.register(r'parent', ParentViewSet)  # Register the viewset
router.register(r'parent', ClassesViewSet)  # Register the viewset
urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated URLs
]