from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = 'myblog.myadmin.MyAdminSite'