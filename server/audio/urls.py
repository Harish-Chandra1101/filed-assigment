from django.urls import path
from .views import AudioFileView

urlpatterns = [
    path('fetch/<str:audioFileType>/', AudioFileView.as_view(actions={
        'get': 'get_audio_file'
    })),
    path('fetch/<str:audioFileType>/<int:audioFileID>/', AudioFileView.as_view(actions={
        'get': 'get_audio_file'
    })),
    path('create/', AudioFileView.as_view(actions={
        'post': 'create_audio_file'
    })),
    path('update/<str:audioFileType>/<int:audioFileID>/', AudioFileView.as_view(actions={
        'put': 'update_audio_file'
    })),
    path('remove/<str:audioFileType>/<int:audioFileID>/', AudioFileView.as_view(actions={
        'delete': 'delete_audio_file'
    })),
]
