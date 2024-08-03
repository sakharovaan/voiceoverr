# voiceoverr
Simple script for generating tts voices using coqui based on "screenplay"


Easy howto

For English text (vats-vits):

1. Run docker container `docker run -d -v $(pwd):/voices -v $(pwd):/root/.local/share/tts/ --name coqui --entrypoint /bin/sleep ghcr.io/coqui-ai/tts-cpu 100d`
2. `docker exec -it coqui /bin/bash`
3. `python3 /voices/run.py`


For Russian text (silero):
1. `pip install torch`
2. `python3 run-ru.py`