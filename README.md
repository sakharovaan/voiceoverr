# voiceoverr
Simple script for generating tts voices using coqui based on "screenplay"


Howto

## First step -- tts

For English text (vats-vits):

1. Run docker container `docker run -d -v $(pwd):/voices -v $(pwd):/root/.local/share/tts/ --name coqui --entrypoint /bin/sleep ghcr.io/coqui-ai/tts-cpu 100d`
2. `docker exec -it coqui /bin/bash`
3. `python3 /voices/run-coqui.py`


For Russian text (silero+so-vits-svc):
1. `pip install torch`
2. `virtualenv -p python3 --system-site-packages so-vits-svc`
3. `source so-vits-svc/bin/activate`
4. `pip install so-vits-svc-fork`
5. `python3 run-silero.py`


Example screenplay:

```yaml
text: |
    a Привет, мир!

actor_mappings:
  a: xenia

rvc_revoice:
  a: 
    model: /mnt/g/so-vits-svc-fork/saya-model/G_10000.pth
    config: /mnt/g/so-vits-svc-fork/saya-model/config.json
    speaker: ru-saya
```