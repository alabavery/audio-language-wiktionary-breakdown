import re

# search for the headers of each section
# Headers use two or more leading and trailing equals:
# ===Verb=== or ==Pronunciation== or ====Derived terms====
PC = {
    "look_behind": '(?<=\s)', # need preceding whitespace
    "lead_equals": '==+', 
    "title": '[A-Z][\w\s-]+', # "Verb" or "Derived terms" or "Something-else", e.g.
    "trail_equals": '==+',
    "look_ahead": '(?=\s)', # need trailing whitespace
}
PATTERN = re.compile(PC["look_behind"] + PC["lead_equals"] + PC["title"] + PC["trail_equals"] + PC["look_ahead"])


# given a language section, output { [section name]: <text> }
def _get_raw(language_section):
     # kind of silly, but this ensures every header is preceded by whitespace, which allows us to handle them all with the same regex look-behind 
    ls = "\n" + language_section
    header_matches =[(match.group(0), match.span()) for match in re.finditer(PATTERN, ls)]

    final = dict()
    for i, match in enumerate(header_matches):
        header, header_span = match
        content_start = header_span[1]

        is_last = i == len(header_matches) - 1
        if is_last:
            content_end = len(ls) - 1
        else:
            _, next_header_span = header_matches[i+1]
            content_end = next_header_span[0]

        final[header] = ls[content_start:content_end]

    return final


def _clean_header(header):
    return header.replace("=", "").lower()


def get_sub_sections(language_section):
    raw_sub_sections = _get_raw(language_section)
    return {_clean_header(header): content for header, content in raw_sub_sections.items()}
