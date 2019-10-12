# Subtitle Synchronizer
This is a Python3 script written by me out of laziness to synchronize subtitles for movies or TV series or anime or others. In VLC and other media players there are UI based options to sync them with the video but they seems time consuming to use to me, doesn't have clear instructions and doesn't work properly. I could never make use of it. This file takes care of this problem. 

# How to run this file
## What do you need to run this file
1. Python3 
2. Subtitle files

## How to run it
This code takes two parameters. 
You can run this line from command line to know how to use it. 

```
python3 subsync.py -h
```

Output says - 

```
usage: subsync.py [-h] -f FILENAME -t DIFF

optional arguments:
  -h, --help            			show this help message and exit
  -f FILENAME, --file FILENAME 		input subtitle file name
  -t DIFF, --time DIFF              input positive (speed up subtitle) or negative number (speed down subtitle)
```

## Example usage
At first, copy this python file in the directory the subtitle file is in. 
Or, if you are in Linux and if you feel like it, keep this python file in a directory and add that path to the `~/.bashrc` file. Then go to the directory your subtitle file is in. 

### Go FORWARD
Suppose you are in a directory which has a subtitle file named `subtitle.srt`. Now you want to fasten (go forward) this subtitle by 15 seconds. You have to run this line - 

```python
python3 subsync.py -f subtitle.srt -t 15
```
Your subtitle file will be modified and changed.

### Go BACKWORD
Suppose you want to backword by 15 seconds. Just input a negative number as the time value (-15). For example - 

```python
python3 subsync.py -f subtitle.srt -t -15
```
 

## Note
1. You can also use `--file` instead of `-f` and `--time` instead of `-t`. 
2. If you find any bug feel free to create an issue or mail me at `shamiulhasan93@gmail.com`. 

Thank you. 
