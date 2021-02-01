import sys
import os
import json

def get_variables():
    original_args = sys.argv[1:]
    language_env = os.environ['TARGET_LANGUAGE']

    if len(original_args) < 4 and language_env is not None:
        args = original_args + [language_env]
    else:
        args = original_args

    if len(args) != 4:
        print("You provided arguments: {}".format(original_args))
        got_env = language_env is not None
        print("You {} env varibable TARGET_LANGUAGE".format("provided" if got_env else "did not provide"))
        print("You must provide the following positional arguments:")
        print("path to words directory")
        print("path to pages directory")
        print("path to target directory")
        print("language (can be positional argument or env variable 'TARGET_LANGUAGE')")
        raise RuntimeError()

    return args

def get_sources(words_dir, source_dir):
    file_names = os.listdir(source_dir)
    words_and_paths = [(f.split(".")[0], os.path.join(source_dir, f)) for f in file_names]

    with open(os.path.join(words_dir, 'words.json'), 'r') as f:
        words_to_target = json.loads(f.read())
    
    return [w_and_p for w_and_p in words_and_paths if w_and_p[0] in words_to_target]