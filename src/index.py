"""
produces
[
    {
        word: string,
        parts: [
            name: string, // "verb" or "pronunciation", e.g.
            tokens: string[]
        ]
    }
]
"""
import sys
import os
import json

from breakdown import main
from write_batch import write

source_dir, target_dir = sys.argv[1:3]
language = os.environ.get('TARGET_LANGUAGE')

source_files = os.listdir(source_dir)
count = 0
batch = []

for file_name in source_files:
    path = os.path.join(source_dir, file_name)
    if not os.path.isfile(path):
        print("Skipping {f}, since it is a directory".format(f=file_name))
        continue
    
    word, _ = file_name.split(".")    
    batch.append({
        "word": word,
        "parts": main(path, language),
    })

    count += 1
    if len(batch) == 50:
        write(batch, count, target_dir)
        batch = []

if len(batch) > 0:
    write(batch, count, target_dir)
