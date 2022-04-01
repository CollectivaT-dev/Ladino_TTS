import argparse
import sys
import os

def find_all(path):
    for root, dirs, files in os.walk(path):
        for dirs in dirs:
            print("Folder: ",dirs)
            wav = []
            txt = []
            incopleted = []
            for root_f, dirs_f, files_f in os.walk(path+"/"+dirs):
                for f in files_f:
                    if f.find(".wav") != -1:
                        wav.append(f)
                    else:
                        txt.append(f)
                for w in wav:
                    flag = 0
                    for t in txt:
                        if w[:len(w)-3] == t[:len(t)-3]:
                            flag = 1
                            break
                    if flag == 0:
                        incopleted.append(w)
            print("Los textos que faltan son: ",incopleted)
    
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
