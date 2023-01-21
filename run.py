import yaml
from TTS.api import TTS

CONFIG_PATH = '/voices/screenplay.yaml'
OUTPUT_PATH = '/voices/voices'

config = yaml.safe_load(open(CONFIG_PATH))

lines = config['text'].splitlines()

tts = TTS(model_name=config['model'], progress_bar=False, gpu=False)

for i, line in enumerate(lines):
    speaker = line.split(' ')[0]
    text = ' '.join(line.split(' ')[1:])
    voice = config['actor_mappings'][speaker]
    
    filename = f'{i}_{speaker}_'
    for i in text:
        if i.isalpha():
            filename = "".join([filename,i])
    filename += '.wav'

    print(f"{speaker} ({voice}): {text} -> {filename}")

    tts.tts_to_file(text=text, speaker=voice, file_path=f"{OUTPUT_PATH}/{filename}")

