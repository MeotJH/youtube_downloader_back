from flask_restx import Namespace

downloader_api = Namespace(name='download', path='/download', description='gpt관련된 API 모음')