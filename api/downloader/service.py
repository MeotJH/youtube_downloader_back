import yt_dlp

YOUTUBE_URL = 'https://www.youtube.com/watch?v='
def download_video(url):
    down_load_url = YOUTUBE_URL + url
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'verbose': True,  # 디버깅 로그 활성화
    }
    
    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([down_load_url])
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(down_load_url)
        video_filename = ydl.prepare_filename(result)
    return video_filename
