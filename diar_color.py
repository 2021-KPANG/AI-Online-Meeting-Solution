import numpy as np
import re

def make_speaker_map(filename) :
    speaker_map = {}
    with open("./static/text_files/{}".format(filename)) as f:
        text = f.read()
        for t in text.split('\n'):
            speaker_map[t[:9]] = tuple(np.random.choice(range(256), size=3))
    return speaker_map

def setcolor(filename, speaker_map):
    with open("./static/text_files/{}".format(filename)) as f:
        text = f.read()
        if "dr_sum_file" in filename:
            text = text_transform(text)
        s=''
        for t in text.split('\n'):
            spk_str = t[:9]
            if "speaker" not in spk_str:
                    s = s+'<p style="color:rgb{};">'.format((0,0,0)) + t + '</p>\n'
            elif "speakers" in spk_str :
                s = s+'<p style="color:rgb{};">'.format(tuple(np.random.choice(range(256), size=3))) + t + '</p>\n'
            else :
                s = s + '<p style="color:rgb{};">'.format(speaker_map[spk_str]) + t + '</p>\n'
    return s



def text_transform(text) :
    text = text.replace('Speaker', 'speaker')
    text = text.replace('\n','')
    text = text.replace('The speaker', 'speaker')
    text = text.replace('speaker','\nspeaker')
    return text
