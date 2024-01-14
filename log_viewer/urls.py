import django

if django.VERSION >= (2, 0):
    from django.urls import re_path
else:
    from django.conf.urls import url as re_path

from .views import (log_json, log_viewer, log_download, log_entries_view, toggle_live_view, log_files_view,
                    file_log_entries_view)

app_name = "log_viewer"

urlpatterns = [
    re_path(
        r"^json/(?P<file_name>[\.\w-]*)/(?P<page>[0-9]+)$",
        log_json,
        name="log_json_view",
    ),
    re_path(
        r"^json/(?P<file_name>[\.\w-]*)$",
        log_json,
        name="log_json_view",
    ),
    re_path(
        r"^download/single-file/$",
        log_download,
        name="log_download_file_view",
    ),
    re_path(
        r"^download.zip$",
        log_download,
        name="log_download_zip_view",
    ),
    re_path(
        r"^$",
        log_viewer,
        name="log_file_view",
    ),
    re_path(r'^log_entries/$', log_entries_view, name='log_entries'),
    re_path(r'^file_log_entries/(?P<file_name>[\w\.-]+)/$', file_log_entries_view, name='file_log_entries'),
    re_path(r'^toggle_live/(?P<event>[0-9]+)$', toggle_live_view, name='toggle_live'),
    re_path(r'^log_files/$', log_files_view, name='log_files'),
]
