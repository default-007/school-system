from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.DashView.as_view(), name="ad_dash"),
    # path('pa_dash', views.ParentDashView.as_view(), name='pa_dash'),
    # path('te_dash', views.TeacherDashView.as_view(), name='te_dash'),
    # path("programmes/", views.ProgrammesView.as_view(), name="admin_programmes"),
    # path("events/", views.EventsView.as_view(), name="admin_events"),
    # path("news/", views.NewsView.as_view(), name="admin_news"),
    # path("careers/", views.CareerView.as_view(), name="admin_career"),
    # path("gallery/", views.GalleryView.as_view(), name="admin_gallery"),
    # path("class/<int:pk>/", views.StudentsListView.as_view(), name="student"),
    # path("student/create/", views.create_student, name="create_student"),
    # path("student/<id>/", views.student_profile, name="student_profile"),
    # path("classlist", views.ClassListView.as_view(), name="classlist"),
    # re_path(r"^students/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?",
    #   views.StudentView.as_view(),
    #  name="students",),
    # Matches any html file
    # re_path(r"^.*\.*", views.pages, name="pages"),
]
