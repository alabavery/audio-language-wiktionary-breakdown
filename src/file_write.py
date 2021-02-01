import json
import os


def write_success(word, data, target_directory):
    with open(os.path.join(target_directory, "successes", "{}.json".format(word)), 'w+') as f:
        f.write(json.dumps(data))


def write_errors(errors, target_directory):
    with open(os.path.join(target_directory, "errors.json"), 'w+') as f:
        f.write(json.dumps(errors))
