import torch
import os
import yaml


CONFIG_PATH = 'screenplay-ru.yaml'
OUTPUT_PATH = 'voices'


config = yaml.safe_load(open(CONFIG_PATH))
lines = config['text'].splitlines()


device = torch.device('cuda') # change to cpu
local_file = 'v4_ru.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                   local_file)  

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)


for i, line in enumerate(lines):
    speaker = line.split(' ')[0]
    text = ' '.join(line.split(' ')[1:])
    voice = config['actor_mappings'][speaker]
    if ';' in voice:
        pitch = voice.split(';')[1]
    else:
        pitch = None
    
    filename = f'{i}_{speaker}_'
    for i in text:
        if i.isalpha():
            filename = "".join([filename,i])
    filename = filename[0:30]
    filename += '.wav'

    print(f"{speaker} ({voice}): {text} -> {filename}")

    if pitch:
        ssml_text = f'<speak><p><prosody pitch="{pitch}">{text}</prosody></p></speak>'
    else:
        ssml_text = f"<speak><p>{text}</p></speak>"
    print(ssml_text)

    audio_paths = model.save_wav(ssml_text=ssml_text, speaker=voice.split(';')[0], sample_rate=48000, audio_path=f"{OUTPUT_PATH}/{filename}")
