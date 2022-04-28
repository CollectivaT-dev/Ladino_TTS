import os

# Trainer: Where the ✨️ happens.
# TrainingArgs: Defines the set of arguments of the Trainer.
from trainer import Trainer, TrainerArgs

# GlowTTSConfig: all model related values for training, validating and testing.
from TTS.tts.configs.glow_tts_config import GlowTTSConfig

# BaseDatasetConfig: defines name, formatter and path of the dataset.
from TTS.tts.configs.shared_configs import BaseDatasetConfig, BaseAudioConfig, CharactersConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.glow_tts import GlowTTS
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.utils.audio import AudioProcessor

# we use the same path as this script as our training folder.
output_path = os.path.dirname(os.path.abspath(__file__))

# DEFINE DATASET CONFIG
# Set LJSpeech as our target dataset and define its path.
# You can also use a simple Dict to define the dataset and pass it to your custom formatter.
dataset_config = BaseDatasetConfig(
    name="ljspeech",
    meta_file_train="metadata.csv",
    path="/homedtcl/rzevallos/TTS/recipes/ljspeech/LJSpeech-1.1"
)

audio_config = BaseAudioConfig(
    sample_rate=16000,
)

character_config = CharactersConfig(
    pad="_",
    eos= "*",
    bos="^",
    characters="ABCDEFGHIJKLMNOPRSTUVXYZabcdefghijklmnopqrstuvwxyzÇÖÜâçèöúüğİıŞşáéíóúÁÉÍÓÚ",
    punctuations="!'(),-.:;? ",
    phonemes="",
    #phonemes="abcdefhijklmnopqrstuvwxyz\u00e6\u00e7\u00f0\u00f8\u0127\u014b\u0153\u01c0\u01c1\u01c2\u01c3\u0250\u0251\u0252\u0253\u0254\u0255\u0256\u0257\u0258\u0259\u025a\u025b\u025c\u025e\u025f\u0260\u0261\u0262\u0263\u0264\u0265\u0266\u0267\u0268\u026a\u026b\u026c\u026d\u026e\u026f\u0270\u0271\u0272\u0273\u0274\u0275\u0276\u0278\u0279\u027a\u027b\u027d\u027e\u0280\u0281\u0282\u0283\u0284\u0288\u0289\u028a\u028b\u028c\u028d\u028e\u028f\u0290\u0291\u0292\u0294\u0295\u0298\u0299\u029b\u029c\u029d\u029f\u02a1\u02a2\u02c8\u02cc\u02d0\u02d1\u02de\u03b2\u03b8\u03c7\u1d7b\u2c71"
)

# INITIALIZE THE TRAINING CONFIGURATION
# Configure the model. Every config class inherits the BaseTTSConfig.
config = GlowTTSConfig(
    run_name="Eng_Lad",
    run_description="English_Ladino_test",
    batch_size=32,
    eval_batch_size=16,
    num_loader_workers=4,
    num_eval_loader_workers=4,
    run_eval=True,
    test_delay_epochs=-1,
    epochs=5000,
    text_cleaner="multilingual_cleaners",
    use_phonemes=False,
    phoneme_language="en-us",
    #phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
    print_step=25,
    print_eval=False,
    mixed_precision=True,
    output_path=output_path,
    datasets=[dataset_config],
    audio=audio_config,
    characters=character_config,
    test_sentences=["Hello my name is Rodolfo","Hello my name is Eva"],
)

# INITIALIZE THE AUDIO PROCESSOR
# Audio processor is used for feature extraction and audio I/O.
# It mainly serves to the dataloader and the training loggers.
ap = AudioProcessor.init_from_config(config)

# INITIALIZE THE TOKENIZER
# Tokenizer is used to convert text to sequences of token IDs.
# If characters are not defined in the config, default characters are passed to the config
tokenizer, config = TTSTokenizer.init_from_config(config)

# LOAD DATA SAMPLES
# Each sample is a list of ```[text, audio_file_path, speaker_name]```
# You can define your custom sample loader returning the list of samples.
# Or define your custom formatter and pass it to the `load_tts_samples`.
# Check `TTS.tts.datasets.load_tts_samples` for more details.
train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True)

# INITIALIZE THE MODEL
# Models take a config object and a speaker manager as input
# Config defines the details of the model like the number of layers, the size of the embedding, etc.
# Speaker manager is used by multi-speaker models.
model = GlowTTS(config, ap, tokenizer, speaker_manager=None)

# INITIALIZE THE TRAINER
# Trainer provides a generic API to train all the 🐸TTS models with all its perks like mixed-precision training,
# distributed training, etc.
trainer = Trainer(
    TrainerArgs(), config, output_path, model=model, train_samples=train_samples, eval_samples=eval_samples
)

# AND... 3,2,1... 🚀
trainer.fit()
