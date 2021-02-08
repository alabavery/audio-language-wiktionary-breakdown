import sys
import os
import json

from breakdown import main
from file_write import write_success, write_errors
import get_input


words_dir, source_dir, target_dir, language = get_input.get_variables()
os.makedirs(os.path.join(target_dir, "successes"), exist_ok=True)

source_words_and_paths = get_input.get_sources(words_dir, source_dir)
errors = []

for word, path in source_words_and_paths:
    try:
        write_success(word, main(path, language), target_dir)
    except Exception as e:
        errors.append({"word": word, "error": str(e)})
        continue

print("Done. {num} errors.".format(num=len(errors)))
write_errors(errors, target_dir)
