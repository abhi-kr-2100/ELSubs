# ELSubs

Using the `elsubs.sh` script, one can extract subtitles from videos in the [Easy Languages](https://www.youtube.com/c/learnlanguages/) format.

## Installation

Make sure you've the following tools installed and available on your `PATH` variable:

* yt-dlp
* ffmpeg
* convert (part of ImageMagik)
* tesseract

Afterwards, just put `elsubs.sh` to a convinient location.

## Usage

To extract subtitles from an Easy Languages video, you'll first need its ID. The ID is part of the video's URL: `https://www.youtube.com/watch?v=ID`. Next, you need to find the language code for the primary language of the video (the language the video is attempting to teach).

Finally, run `elsubs.sh` with the ID passed as the first argument and the language code as the second. An example run is shown below:

```sh
$ elsubs.sh AdYiOoBzhHI tur
...
```

After the script finishes, a new directory will have been created. Inside the directory you'll find two text files, `{ID}.top.txt` containing text in the primary language and `{ID}.bottom.txt` containing text in English.
