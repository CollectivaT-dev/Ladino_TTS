# Judeo-Espanyol TTS 📢🤖
Judeo-Espanyol TTS (text-to-speech) using Coqui TTS.

# Example

https://user-images.githubusercontent.com/5759207/149566245-40656002-3999-48a8-b671-e0f74c3d6e2f.mp4

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
