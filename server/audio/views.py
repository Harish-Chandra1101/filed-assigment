from rest_framework import viewsets, status
from rest_framework.response import Response
from .handler import AudioFileHandler

class AudioFileView(viewsets.ViewSet):

    def create_audio_file(self, request):
        resp_data = AudioFileHandler.create_audio_file(request)
        if resp_data.get('errors'):
            status_obj = status.HTTP_400_BAD_REQUEST
        else:
            status_obj = status.HTTP_200_OK
        return Response(
            data=resp_data,
            status=status_obj
        )

    def update_audio_file(self, request, **kwargs):
        resp_data = AudioFileHandler.update_audio_file(request, kwargs)
        if resp_data.get('errors'):
            status_obj = status.HTTP_400_BAD_REQUEST
        else:
            status_obj = status.HTTP_200_OK
        return Response(
            data=resp_data,
            status=status_obj
        )
