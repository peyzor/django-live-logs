import django

if django.VERSION >= (2, 0):
    from django.urls import re_path
else:
    from django.conf.urls import url as re_path

from .views import (log_json, log_viewer, log_download, FileLogEntryListView, ToggleLiveView,
                    LogFileListView)

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
    re_path(r'^log-files/$', LogFileListView.as_view(), name='log_files'),
    re_path(r'^file-log-entries/(?P<filename>[\w\.-]+)/$', FileLogEntryListView.as_view(), name='file_log_entries'),
    re_path(r'^toggle-live/(?P<event>\d+)/(?P<filename>[\w\.-]+)/$', ToggleLiveView.as_view(), name='toggle_live'),
]
