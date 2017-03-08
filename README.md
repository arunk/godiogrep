# About
These set of files downloads videos from the PornHub website, strip the audio from the video files and run an audio transcription tool called audiogrep on the audio files. Video files are downloaded to ./video and stripped audio files and transcribed text files to ./audio

# Install
Use with [virtualenv](https://virtualenv.pypa.io/en/stable/) if possible, otherwise to install system-wide ensure that you have installed [pip](https://pip.pypa.io/en/stable/installing/) then run the following in a shell

    $ sudo pip install -r requirements.txt

Leave out the sudo if you installing it inside a virtual environment.

# Running
Open main.py and edit the following if required:

SEARCH_PHRASES - add search phrases to this list. the videos listed on the search result pages of these phrases will be downloaded

NUM_PAGES - the maximum number of pages of search results to download videos from.

MAX_DURATION - the longest duration of video to download.

Now run 

    $ python main.py

This might take a few hours to run depending on the number of search phrases, number of pages, maximum duration, internet connection speed etc.

Then run

    $ bash process.sh

This might take a few hours again depending on the number of videos downloaded.

# Finding god
Use grep

    $ grep -lir "god" audio/*.txt
