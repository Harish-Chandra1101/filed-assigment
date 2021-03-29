from .serializers import (
    SongFileSerializer,
    PodcastFileSerializer,
    AudiobookFileSerializer,
)
from .models import (
    Song,
    Podcast,
    Audiobook,
)
from utils.responses import GenericResponse
from .constants import VALID_FILE_TYPES
from django.core.exceptions import ObjectDoesNotExist

class AudioFileHandler:

    @staticmethod
    def create_audio_file(request):
        file_type = request.data.get('audioFileType') or ''
        serializer_class = AudioFileHandler.get_serializer_class(file_type)
        if not serializer_class:
            return GenericResponse.get_error_response(
                msg='Invalid File type'
            )
        file_data = request.data.get('audioFileMetadata') or {}
        serial_obj = serializer_class(data=file_data)
        if serial_obj.is_valid():
            serial_obj.save()
            return GenericResponse.get_success_response(
                data=f"Audio file of type {file_type} created"
            )
        return GenericResponse.get_error_response(
            msg=serial_obj.errors
        )

    @staticmethod
    def update_audio_file(request, url_args):
        file_data = request.data.get('audioFileMetadata') or {}
        validated_data = AudioFileHandler.get_and_validate_url_args(url_args)
        if not validated_data['valid']:
            return GenericResponse.get_error_response(
                msg=validated_data['msg']
            )
        file_type = validated_data['file_type']
        file_id = validated_data['file_id']
        model = {
            'Song': Song,
            'Podcast': Podcast,
            'Audiobook': Audiobook,
        }.get(file_type)
        audio_file = model.objects.filter(pk=file_id)
        if not audio_file:
            return GenericResponse.get_error_response(
                msg=f'Audio file {file_type} not found with id {file_id}'
            )
        serializer_class = AudioFileHandler.get_serializer_class(file_type)
        serial_obj = serializer_class(audio_file, data=file_data, partial=True)
        if serial_obj.is_valid():
            serial_obj.save()
            return GenericResponse.get_success_response(
                data=file_data
            )
        return GenericResponse.get_error_response(
            msg=serial_obj.errors
        )

    @staticmethod
    def get_serializer_class(file_type):
        serializer_class = {
                               'Song': SongFileSerializer,
                               'Podcast': PodcastFileSerializer,
                               'Audiobook': AudiobookFileSerializer,
                           }.get(file_type) or None
        return serializer_class

    @staticmethod
    def get_and_validate_url_args(url_args, id_required=True):
        file_type = url_args.get('audioFileType') or ''
        file_id = url_args.get('audioFileID')
        return_value = {
            'valid': True,
            'file_type': file_type,
            'file_id': file_id,
            'msg': ''
        }
        if not file_type or file_type not in VALID_FILE_TYPES:
            return_value.update({
                'valid': False,
                'msg': 'Invalid file type'
            })
            return return_value
        if not file_id and id_required:
            return_value.update({
                'valid': False,
                'msg': 'File id not present'
            })
            return return_value
        return return_value

    @staticmethod
    def delete_audio_file(request, url_args):
        validated_data = AudioFileHandler.get_and_validate_url_args(url_args)
        if not validated_data['valid']:
            return GenericResponse.get_error_response(
                msg=validated_data['msg']
            )

        file_type = validated_data['file_type']
        file_id = validated_data['file_id']
        model = {
            'Song': Song,
            'Podcast': Podcast,
            'Audiobook': Audiobook,
        }.get(file_type)
        try:
            model.objects.get(pk=file_id).delete()
            return GenericResponse.get_success_response(
                data=f'Audio file type {file_type} with id {file_id} deleted'
            )
        except ObjectDoesNotExist as e:
            return GenericResponse.get_error_response(
                msg=str(e)
            )

    @staticmethod
    def get_audio_file(request, url_args):
        validated_data = AudioFileHandler.get_and_validate_url_args(url_args, id_required=False)
        file_type = validated_data['file_type']
        file_id = validated_data['file_id']
        model = {
            'Song': Song,
            'Podcast': Podcast,
            'Audiobook': Audiobook,
        }.get(file_type)
        if file_id:
            try:
                obj = model.objects.get(pk=file_id)
                ser_class = AudioFileHandler.get_serializer_class(file_type)
                ser_data = ser_class(obj).data
                return GenericResponse.get_success_response(
                    data=ser_data
                )
            except ObjectDoesNotExist as e:
                return GenericResponse.get_error_response(
                    msg=str(e)
                )
        query_set = model.objects.all()
        return GenericResponse.get_success_response(
            data=query_set.values()
        )
