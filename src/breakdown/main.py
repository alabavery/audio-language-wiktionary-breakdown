from breakdown.get_language_section import get_language_section
from breakdown.get_sub_sections import get_sub_sections

def main(page_text, language):
    language_section = get_language_section(page_text, language)
    
    parts = []
    for section_name, section in get_sub_sections(language_section).items():
        parts.append({
            "name": section_name,
            "tokens": [line for line in section.split('\n') if line != '']
        })

    return parts