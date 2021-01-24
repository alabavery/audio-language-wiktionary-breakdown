import json
import os


def write(batch, count, target_directory):
    file_name = "{first_num}-{last_num}___{first_word}-{last_word}.json".format(
        first_num=count-len(batch),
        last_num=count-1,
        first_word=batch[0]["word"],
        last_word=batch[-1]["word"],
    )
    with open(os.path.join(target_directory, file_name), 'w+') as f:
        f.write(json.dumps(batch))

    print("Saved batch: {file_name}".format(file_name=file_name), flush=True)
