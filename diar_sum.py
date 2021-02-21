def speaker(x):
    talk_str = x.split("\n")
    total = []

    speaker_num = 0
    for i in talk_str:
        try:
            if int(i[8]) > speaker_num:
                speaker_num = int(i[8])
        except:
            pass

    num = 0
    speaker_talk = [[] for row in range(speaker_num)]
    for i in talk_str:
        if len(i) > 30:
            try:
                num = int(i[8]) - 1
                j = i[11:].split(".")
                clean_list = []
                for k in j:
                    if len(k) > 2:
                        k = k.strip()
                        total.append(k)
                        clean_list.append(k)
                speaker_talk[num].extend(clean_list)
            except:
                pass
        else:
            pass
    return speaker_talk, speaker_num, total


def bertsum(filename, out_max_length, speaker_talk, speaker_num, total):
    from summarizer import Summarizer

    with open("./static/text_files/{}".format(filename.replace('.txt', '_dr_sum_file.txt')), 'w') as f:
        f.write(" More than " + str(speaker_num) + " people participated... <br>\n")
        for i in range(speaker_num):
            text = ". ".join(speaker_talk[i])
            f.write("speaker " + str(i + 1) + " :<br> ")
            model = Summarizer('distilbert-base-uncased')
            output = model(text, max_length=out_max_length)
            f.write(output + "\n")
        out_text = ". ".join(total)
        total_output = model(out_text, max_length=out_max_length)
        f.write("\nsummary : " + total_output)
    return


def bart(filename, x, total, speaker_num):
    s = "More than " + str(speaker_num) + " people participated..<br>"
    s1 = s + "<br>"
    total = total
    x = x.split("\n")
    bart2(filename, 3, x, s1)
    # bart2(filename, 4, total, "\ntotal")


def bart2(filename, number, y, str):

    from fastai.learner import load_learner
    import torch
    import pickle
    import datasets
    import re
    import pathlib
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath

    inf_learn = load_learner(fname='./data/bart_pretrained_SAMsum.pkl')
    with open("./static/text_files/{}".format(filename.replace('.txt', '_dr_sum_file.txt')), 'w') as f:
        f.write(str + "\n")
        num = 0
        s = ''
        llist = []
        for i in range(len(y)):
            s = s + y[i]
            if num == number:
                llist.append(s)
                num = 0
                s = ''
            num += 1
        ll = []
        for i in llist:
            tt = inf_learn.blurr_generate(i)
            a = tt.pop()
            a = a.strip()
            # a1 = re.sub(r'\([^)]*\)', '', a)
            ll.append(a)
            print(a)
        for i in ll:
            f.write(i + "\n")
    return
