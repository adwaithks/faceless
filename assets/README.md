## script.txt

This file contains the narrative / story which we want to tell.
Should consist of multiple sentences separated by a new line. An image will
be generated for each line in this file.

## subtitles.txt

This file is exactly same as `script.txt`. But the only difference is that
it is a broken down version of `script.txt`. Meaning, each line in `script.tx`
is broken down into 2 or more lines in `subtitles.txt`. An audio file will be generated for each line in this file, which will form the subtitle as well.

## Important

`script.txt` and `subtitle.txt` should be containing the same contents except for the fact that each line in `script.txt` is broken down into 2 or more lines in `subtitle.txt`.

```
Eg:

script.txt
-----------
This is the first line followed by something.
This is the second line.

subtitle.txt
-------------
This is the first line
followed by something.
This is the second line.
```

Here each line in `subtitle.txt` will appear as subtitle in the video, therefore currently it is required that the words should match the `script.txt`, eventhough this requirement will not be needed in the future to make things easy.
