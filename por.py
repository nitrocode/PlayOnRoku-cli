#!/usr/bin/env python3
from urllib.parse import urlparse
import urllib.parse
import sys
import requests
from roku import Roku


def valid_url(url):
    """Return true if the url is valid."""
    try:
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc, parsed.path])
    except:
        return False


def roku_url():
    """Return the roku url using SSDP discovery."""
    rok = Roku.discover(timeout=5)
    if len(rok) > 0:
        return 'http://{}:{}'.format(rok[0].host, rok[0].port)


if __name__ == "__main__":
    # get url and urlformat as the first param
    try:
        vurl = sys.argv[1]
        if not valid_url(vurl):
            print("Invalid url: {}".format(vurl))
            sys.exit(0)
    except:
        vurl = "https://player.vimeo.com/play/12943877?s=1084537_1531865731_824ddbf60f1d377f51ff1e9affc71759&loc=external&context=Vimeo%5CController%5CClipController.main&download=1"

    # valid formats: https://support.roku.com/article/208754908-how-to-use-roku-media-player-to-play-your-videos-music-and-photos
    try:
        vformat = sys.argv[2]
    except:
        vformat = 'mp4'

    # title is optional
    try:
        name = sys.argv[3]
    except:
        name = 'idgaf'

    # urlencode the url
    vurl = urllib.parse.quote_plus(vurl)

    # construct the POST to the Roku
    # 15985 is the channel id for PlayOnRoku
    url = '{}/input/15985?t=v&u={}&videoName={}&k=(null)&videoFormat={}'.format(
        roku_url(), vurl, name, vformat
    )
    # print reproducible curl statement
    print("curl -d '' '{}'".format(url))
    #req = urllib.request.Request(url, data=''.encode('ascii'))
    res = requests.post(url)
