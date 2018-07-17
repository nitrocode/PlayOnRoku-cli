# PlayOnRoku-cli

CLI app to quickly cast an mp4 from a url to Roku using PlayOnRoku built in channel app.

## Prereq

* Port 1900 UDP should be open to detect the Roku via SSDP
* Install `pipenv`

        pip install pipenv

* Install

        pipenv install

## Usage

    ./por.py http://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4

Output

    curl -d '' 'http://192.168.1.33:8060/input/15985?t=v&u=http%3A%2F%2Fdownload.blender.org%2Fpeach%2Fbigbuckbunny_movies%2FBigBuckBunny_320x180.mp4&videoName=idgaf&k=(null)&videoFormat=mp4'

## TODO

- [ ] `argparse` instead of `sys.argv`
- [ ] override roku IP using config file and `argparse`
- [ ] single binary using `pyinstaller` or similar or convert to go
