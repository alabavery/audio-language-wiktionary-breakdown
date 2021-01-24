import sys

from breakdown.main import main as breakdown

def main(page_path, language):
    with open(page_path, "r") as f:
        page_text = f.read()
    return breakdown(page_text, language)

if __name__ == '__main__':
    page_path, language = sys.argv[1:3]
    print(main(page_path, language))