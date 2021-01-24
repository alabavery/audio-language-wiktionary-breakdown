docker rm -f wiktionary-breakdown;
docker rmi alaverydev/audio-language-wiktionary-breakdown;
docker build -t alaverydev/audio-language-wiktionary-breakdown .
docker push alaverydev/audio-language-wiktionary-breakdown