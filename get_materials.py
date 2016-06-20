# -*- coding: utf-8 -*-

import csv
import json
import os
import time

# get materials
materials_file = "manifest.csv"
materials = []
with open(materials_file, 'rb') as f:
    r = csv.DictReader(f)
    for row in r:
        materials.append(row)
print "%s items found" % len(materials)

def printInfo(item):

    with open(item["transcript_json"]) as data_file:
        transcript = json.load(data_file)
        print "Loaded the transcript for %s" % item["title"]

        # print duration
        print "The duration is: %s" % time.strftime("%H:%M:%S", time.gmtime(transcript["duration"]))

        # get the word count
        lines = [l["best_text"] for l in transcript["lines"]]
        content = " ".join(lines)
        words = content.split(" ")
        print "The word count is: %s" % len(words)

    # view the audio file
    filename = os.path.basename(item["audio"])
    fileBytes = os.path.getsize(item["audio"])
    print "Audio file %s is size %sMB" % (filename, round(0.000001 * fileBytes))

# take the first item as an example
example = materials[0]
printInfo(example)
