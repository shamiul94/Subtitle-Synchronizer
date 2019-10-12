# @author: Shamiul Hasan (Heisenberg), BUET CSE
# Date: 3:45 PM (BDT), Oct 12, 2019
# Email: shamiulhasan93@gmail.com
# github: shamiul94


import os
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-f", "--file", type=str, dest="filename", required=True,
                    help="input subtitle file name")

parser.add_argument("-t", "--time",
                    required=True, type=int, dest="diff", default=0,
                    help="input positive (speed up subtitle) or negative (speed down subtitle) number of seconds.")

args = parser.parse_args()
dir_path = str(os.path.dirname(os.path.realpath(__file__)))
diff = args.diff
filename = dir_path + '/' + args.filename

with open(filename) as f:
    content = f.readlines()

content = [x for x in content]

fw = open(filename, "w")
for x in content:
    if x.strip().__contains__('-->'):
        line = x.strip().split(' --> ')
        first = line[0]
        second = line[1]

        firstTimeWithoutMS = first.split(',')[0]
        firstMS = first.split(',')[1]
        secondTimeWithoutMS = second.split(',')[0]
        secondMS = second.split(',')[1]

        firstHour = int(firstTimeWithoutMS.split(':')[0])
        firstMinute = int(firstTimeWithoutMS.split(':')[1])
        firstSecond = int(firstTimeWithoutMS.split(':')[2])

        secondHour = int(secondTimeWithoutMS.split(':')[0])
        secondMinute = int(secondTimeWithoutMS.split(':')[1])
        secondSecond = int(secondTimeWithoutMS.split(':')[2])

        firstTime = firstHour * 60 * 60 + firstMinute * 60 + firstSecond + diff
        secondTime = secondHour * 60 * 60 + secondMinute * 60 + secondSecond + diff

        firstHour = int(firstTime / 3600)
        firstMinute = int((firstTime % 3600) / 60)
        firstSecond = int(((firstTime % 3600) % 60))

        secondHour = int(secondTime / 3600)
        secondMinute = int((secondTime % 3600) / 60)
        secondSecond = int(((secondTime % 3600) % 60))

        # format = 02:39:53,500 --> 02:39:54,859

        finalLine = str(firstHour).zfill(2) + ':' \
                    + str(firstMinute).zfill(2) + ':' \
                    + str(firstSecond).zfill(2) + ',' \
                    + firstMS + ' --> ' \
                    + str(secondHour).zfill(2) + ':' \
                    + str(secondMinute).zfill(2) + ':' \
                    + str(secondSecond).zfill(2) + ',' + secondMS

        fw.write(finalLine + '\n')

    else:
        fw.write(x)

fw.close()
