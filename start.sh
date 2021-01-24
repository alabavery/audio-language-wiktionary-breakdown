docker run \
    --name=wiktionary-breakdown \
    -v $1:"/pages_directory_mount" \
    -v $2:"/target_directory_mount" \
    -e TARGET_LANGUAGE=$3 \
    alaverydev/audio-language-wiktionary-breakdown