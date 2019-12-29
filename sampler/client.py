import os

import requests

from django.conf import settings

def video(item):
    v = {}
    v['id'] = item['id']['videoId']
    v['watch_url'] = 'https://www.youtube.com/watch?v={}'.format(v['id'])
    v['embed_url'] = 'https://www.youtube.com/embed/{}'.format(v['id'])
    v['thumbnail_url'] = item['snippet']['thumbnails']['medium']['url']
    v['title'] = item['snippet']['title']
    return v

def get_videos(keyword):
    key = settings.YOUTUBE_API_KEY,
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': key,
        'part': 'snippet',
        'maxResults': 50,
        'q': keyword,
        'type': 'video',
        'videoDuration': 'short',
    }
        
    response = requests.get(url, params)
    print(response.json())
    items = response.json()['items']
    
    videos = []
    for item in items:
        v = video(item)
        videos.append(v)
    return videos
