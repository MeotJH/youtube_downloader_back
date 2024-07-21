
from api.downloader.service import download_video
from flask_restx import Resource, fields
from flask import  Response,send_file, request
from http import HTTPStatus
import os

from api import downloader_api as api
import json

tts_text_field = fields.String(required=True, title='tts 텍스트 데이터', description="TTS 바이너리로 변환된")

users_response_model = api.model('TTSResponseModel', {
    #'voice': binary_field,
    'text' : tts_text_field,
})

@api.route('/<string:name>', strict_slashes=False)
class YoutubeDownloader(Resource,):
    @api.doc(params={'name': 'Hello World'})
    def get(self, name):
        print(name)
        video_filename = download_video(name)
        absolute_path = os.path.abspath(video_filename)

        if os.path.exists(video_filename):
            return send_file(absolute_path, as_attachment=True, download_name=os.path.basename(absolute_path), mimetype='video/mp4')
        else:
            return "Failed to download video", 500