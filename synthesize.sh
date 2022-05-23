MODELLOC=/Users/alp/Cloud/Projects/Judeo-Esp/Ladino-data-workspace/TTS/Models/Eng_Lad_v2

tts --model_path $MODELLOC/eng_lad_v2_checkpoint_770000.pth --config_path $MODELLOC/eng_lad_v2_config.json \
--out_path ola.wav --text "selebramos muestras companyeras alp pelin i gunes"


tts-server --model_path /Users/alp/Cloud/Projects/Judeo-Esp/Ladino-data-workspace/TTS/Models/Eng_Lad_v2/eng_lad_v2_checkpoint_770000.pth \
--config_path /Users/alp/Cloud/Projects/Judeo-Esp/Ladino-data-workspace/TTS/Models/Eng_Lad_v2/eng_lad_v2_config.json 


#/Users/alp/Library/Application Support/tts/tts_models--uk--mai--glow-tts