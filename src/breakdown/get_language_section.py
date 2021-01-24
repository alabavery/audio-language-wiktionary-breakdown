import re
import sys

any_language_header_matcher = re.compile('\s==[A-Z][\w\s-]+==\s')

# get from ==Spanish== to end of file or to next language
def get_language_section(page_text, language):
    language_header = "=={}==".format(language.capitalize())
    starts_at = page_text.find(language_header)
    if starts_at < 0:
        raise RuntimeError("Did not find start of language")

    after_start = page_text[starts_at + len(language_header):]
    next_language_header_match = any_language_header_matcher.search(after_start)

    if next_language_header_match == None:
        return after_start
    return after_start[:next_language_header_match.start() - 1]


if __name__ == '__main__':
    page_path, language = sys.argv[1:3]
    with open(page_path, 'r') as f:
        t = f.read()
    res = get_language_section(t, language)
    print(res)