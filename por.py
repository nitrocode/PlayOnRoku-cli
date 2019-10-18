#!/usr/bin/env python3
from urllib.parse import urlparse
import urllib.parse
import sys
import requests
from roku import Roku


def valid_url(url: str) -> bool:
    """Return true if the url is valid."""
    try:
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc, parsed.path])
    except TypeError:
        return False


def roku_url() -> str:
    """Return the roku url using SSDP discovery."""
    rok = Roku.discover()
    if len(rok) > 0:
        return 'http://{}:{}'.format(rok[0].host, rok[0].port)
    else:
        return 'http://192.168.1.33:8060'


def main():
    # get url and urlformat as the first param
    try:
        video_url = sys.argv[1]
        if not valid_url(video_url):
            print("Invalid url: {}".format(video_url))
            sys.exit(0)
    except IndexError:
        video_url = "https://player.vimeo.com/play/12943877?s=1084537_1531" + \
                    "865731_824ddbf60f1d377f51ff1e9affc71759&loc=external&" + \
                    "context=Vimeo%5CController%5CClipController.main&down" + \
                    "load=1"

    # valid formats: https://support.roku.com/article/208754908-how-to-use-roku-media-player-to-play-your-videos-music-and-photos
    try:
        vformat = sys.argv[2]
    except IndexError:
        vformat = 'mp4'

    # title is optional
    try:
        name = sys.argv[3]
    except IndexError:
        name = 'idgaf'

    # url encode the url
    video_url = urllib.parse.quote_plus(video_url)

    # construct the POST to the Roku
    # 15985 is the channel id for PlayOnRoku
    url = '{}/input/15985?t=v&u={}&videoName={}&k=(null)&videoFormat={}'.format(
        roku_url(), video_url, name, vformat
    )
    # print reproducible curl statement
    print("curl -d '' '{}'".format(url))
    return requests.post(url)


if __name__ == "__main__":
    main()
