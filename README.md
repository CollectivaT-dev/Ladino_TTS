<p align="center"><img src="https://raw.githubusercontent.com/CollectivaT-dev/Espanyol-Ladino-Translation/master/img/ab-tr.jpg"></p>

# Judeo-Espanyol TTS 📢🤖
Judeo-Espanyol TTS (text-to-speech) using Coqui TTS. 

# Dataset and model checkpoint

Dataset and model available at [Ladino Data hub](https://data.sefarad.com.tr/). 

# Example

https://user-images.githubusercontent.com/5759207/149566245-40656002-3999-48a8-b671-e0f74c3d6e2f.mp4

# Online demo

An online web application with speech synthesis integrated is available at [translate.sefarad.com.tr](https://translate.sefarad.com.tr/).

# How to use :
1. `pip install -r requirements.txt`.
2. Download model from "Releases" tab.
3. Launch as one-time command:  
```
tts --text "Text for TTS" \
    --model_path path/to/model.pth.tar \
    --config_path path/to/config.json \
    --out_path folder/to/save/output.wav
```


# How to train:
1. Refer to ["Nervous beginner guide"](https://tts.readthedocs.io/en/latest/tutorial_for_nervous_beginners.html) in Coqui TTS docs.
2. Instead of provided `config.json` use one from this repo.


# Citation

```
Alp Öktem, Rodolfo Zevallos, Yasmin Moslem, Güneş Öztürk, Karen Şarhon. Preparing an endangered language for the digital age: The Case of Judeo-Spanish. Workshop on Resources and Technologies for Indigenous, Endangered and Lesser-resourced Languages in Eurasia (EURALI) @  LREC 2022. Marseille, France. 20 June 2022
```

---

This repo is developed as part of project "Judeo-Spanish: Connecting the two ends of the Mediterranean" carried out by Col·lectivaT and Sephardic Center of Istanbul within the framework of the “Grant Scheme for Common Cultural Heritage: Preservation and Dialogue between Turkey and the EU–II (CCH-II)” implemented by the Ministry of Culture and Tourism of the Republic of Turkey with the financial support of the European Union. The content of this website is the sole responsibility of Col·lectivaT and does not necessarily reflect the views of the European Union. 
