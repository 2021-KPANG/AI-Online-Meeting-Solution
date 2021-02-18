import numpy as np


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
        s=''
        for t in text.split('\n'):
            spk_str = t[:9]
            if "speaker " not in spk_str:
                if "summary" in spk_str:
                    s = s+'<p style="color:rgb{};"><mark>'.format((0,0,0)) + t + '</mark></p>\n'
                else :
                    s = s+'<p style="color:rgb{};">'.format((0,0,0)) + t + '<br/></p>\n'
            else:
                s = s + '<p style="color:rgb{};">'.format(speaker_map[spk_str]) + t + '</p>\n'
    return s