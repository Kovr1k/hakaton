from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Main.as_view(), name="main"),
    path("testAPI/", TestAPIForm.as_view(), name="test"),
    path("achievements/", Achievements.as_view(), name="achievements"),
    path("addAchievement/", AddAchievements.as_view(), name="addAchievements"),
    path("delete/<part_id>", DeleteView.as_view(), name='delete_view'),
]