#!/usr/bin/env python
#-*- coding: utf-8 -*-

# LICENSE: WTFPL
# This script uses the search phrases in SEARCH_PHRASES to search https://www.pornhub.com/ and downloads
# the videos found in the first NUM_PAGES pages of search results. It will only download all videos
# shorter than MAX_DURATION seconds.

import six
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup
import requests
if six.PY2:
    from urllib import urlencode
else:
    from urllib.parse import urlencode
import os

# The search phrases to use
SEARCH_PHRASES = ["oh god", "orgasm", "intense orgasm"]
NUM_PAGES = 5
MAX_DURATION = 600

if __name__ == '__main__':
    ydl = YoutubeDL({"outtmpl": "./video/%(id)s.%(ext)s", "retries": 5})
    ydl.add_default_info_extractors()

    # download videos a set, since some videos might appear twice under different search phrases
    download_videos = set()
    for search in SEARCH_PHRASES:
        for p in range(1, NUM_PAGES+1):
            # use the search phrase and page number to get the search result page
            scrape = BeautifulSoup(requests.get("https://www.pornhub.com/video/search?{}".format(urlencode({"search": search, "page":p}))).content, "html.parser")
            for a in scrape.find_all("a", "img"):
                info = ydl.extract_info('https://www.pornhub.com{}'.format(a.attrs['href']), download=False)
                if info['duration'] <= MAX_DURATION:
                    #download only if it's not already done
                    if not os.path.exists("./video/{}.mp4".format(info['id'])):
                        download_videos.add("https://www.pornhub.com{}".format(a.attrs['href']))

    ydl.download(list(download_videos))

