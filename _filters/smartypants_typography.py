import smartypants

config = {
    'name': "Smartypants",
    'description': "Translates plain punctuation to typographic punctuation",
    'aliases': ['smartypants']
    }


def run(content):
    return smartypants.smartyPants(content)
