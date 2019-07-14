import json
import re
import urllib.request

TAG = 'v7.2.0'


def split_to_sections(content: str, h: int = 3) -> dict:
    sep = h * '=' + ' '
    terms = content.split(sep)
    res = {}
    for term in terms:
        title, _, body = term.partition('\n')
        res[title.strip()] = body.strip()
    return res


def get_asciidoc(url: str) -> str:
    url = f'https://raw.githubusercontent.com/elastic/elasticsearch/{TAG}/docs/reference/{url}'
    return urllib.request.urlopen(url).read().decode()


def get_section(content: str, section: str) -> str:
    sections = split_to_sections(content)
    return sections[section]


def get_settings(content: str) -> dict:
    blocks = re.split('`(.*)`::', content)[1:]
    return [{"description": blocks[i+1].strip(), "name": blocks[i]} for i in range(0, len(blocks), 2)]


def get_desc(content: str) -> str:
    return re.split('`.*`::', content)[0].strip()


def extract(location: str, section_name: str) -> None:
    content = get_asciidoc(location)
    index_settings = get_section(content, section_name)
    settings = get_settings(index_settings)
    desc = get_desc(index_settings)
    fname = section_name.lower().replace(' ', '_')
    json.dump(
        {"description": desc,
         "settings": settings,
         "name": section_name,
         },
        open(f'../../elasticsearch/index_settings/{fname}.json', 'w'),
        indent=2)


if __name__ == "__main__":
    extract('index-modules.asciidoc', 'Dynamic index settings')
    extract('index-modules/translog.asciidoc', 'Translog settings')
