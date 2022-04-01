import argparse
import sys
import os
import pandas as pd

 
def main():
    df = pd.read_csv("dataset.csv", sep="|")
    text = df["text_norm"]
    data = ""
    for t in text:
        data = data + str(t).replace("\t","") + " "
    final = sorted(set(data))
    final = "".join(a for a in final)
    print(final)



if __name__ == "__main__":
    main()