import sys
import os
import json

from breakdown import main
from file_write import write_batch, write_errors

source_dir, target_dir = sys.argv[1:3]
os.makedirs(os.path.join(target_dir, "successes"), exist_ok=True)
language = os.environ["TARGET_LANGUAGE"]

source_files = os.listdir(source_dir)
count = 0
batch = []
errors = []

for file_name in source_files:
    path = os.path.join(source_dir, file_name)
    if not os.path.isfile(path):
        print("Skipping {f}, since it is a directory".format(f=file_name))
        continue
    
    word, _ = file_name.split(".")
    try:    
        batch.append({
            "word": word,
            "parts": main(path, language),
        })
    except Exception as e:
        print("Problem on word '{word}':".format(word=word))
        print(e)
        errors.append({ "word": word, "error": str(e) })
        continue

    count += 1
    if len(batch) == 50:
        write_batch(batch, count, target_dir)
        batch = []

if len(batch) > 0:
    write_batch(batch, count, target_dir)

print("Done. {num} errors.".format(num=len(errors)))
write_errors(errors, target_dir)