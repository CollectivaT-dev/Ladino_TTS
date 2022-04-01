import argparse
import sys
import os
import pandas as pd

def find_all(path):
    name_wav = []
    text = []
    text_norm = []
    for root, dirs, files in os.walk(path):
        for dirs in dirs:
            wav = []
            txt = []
            for root_f, dirs_f, files_f in os.walk(path+"/"+dirs):
                for f in files_f:
                    if f.find(".wav") != -1:
                        wav.append(f)
                    else:
                        txt.append(f)
                for w in wav:
                    for t in txt:
                        if w[:len(w)-3] == t[:len(t)-3]:
                            name_wav.append(w[:len(w)-4])
                            with open(path+"/"+dirs+"/"+t) as te:
                                te = te.readlines()
                                s = ""
                                for x in te:
                                    s = s + x + " "
                                text_out_norm = " ".join(s.split())
                                text.append(text_out_norm)
                                text_norm.append(text_out_norm)
                            break
    p = {"file": name_wav, "text": text, "text_norm": text_norm}
    df = pd.DataFrame(p)
    df.to_csv("dataset.csv", index=False, sep="|")
    
def main():
    parser = argparse.ArgumentParser("Judeo-Spanish (Ladino) Preprocessing TTS")
    parser.add_argument("-f", "--corpus", help="corpus root.", default=None, required=True)
    args = parser.parse_args()
    root_corpus = args.corpus
    if not args.corpus:
        print("ERROR: No corpus given.")
        sys.exit()
    find_all(root_corpus)
    


if __name__ == "__main__":
    main()
