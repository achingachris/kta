from django.urls import path
from .views import CategoryList, CategoryDetail, AwardList, AwardDetail, NomineeCreate

urlpatterns = [
    path("api/categories/", CategoryList.as_view(), name="category-list"),
    path("api/category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("api/awards/", AwardList.as_view(), name="award-list"),
    path("api/award/<int:pk>/", AwardDetail.as_view(), name="award-detail"),
    path("api/nominees/", NomineeCreate.as_view(), name="nominee-create"),
]
