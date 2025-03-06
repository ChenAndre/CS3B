import json
from enum import Enum
from datalist import DataList, LruCache

class DictionaryEntry:
    def __init__(self, word, part_of_speech, definition, example=None):
        self.word = word
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.example = example

    def __str__(self):
        lines = [
            f"Word          : {self.word}",
            f"Part of speech: {self.part_of_speech}",
            f"Definition    : {self.definition}"
        ]
        if self.example is not None:
            lines.append(f"Example       : {self.example}")
        return '\n'.join(lines)

    def __eq__(self, other):
        if isinstance(other, DictionaryEntry):
            return self.word == other.word
        return False

    def __hash__(self):
        return hash(self.word)

class LocalDictionary:
    def __init__(self, dictionary_json_name="dictionary.json"):
        self.entries = {}
        try:
            with open(dictionary_json_name, 'r') as f:
                data = json.load(f)
                for entry in data['entries']:
                    try:
                        word = entry['word']
                        pos = entry['part_of_speech']
                        definition = entry['definition']
                        example = entry.get('example')
                        self.entries[word] = DictionaryEntry(word, pos, definition, example)
                    except KeyError as e:
                        print(f"Skipping invalid entry: {e}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Dictionary file {dictionary_json_name} not found.")

    def search(self, word):
        if word in self.entries:
            return self.entries[word]
        else:
            raise KeyError(f"Word '{word}' not found in local dictionary")

class DictionarySource(Enum):
    LOCAL = 1
    CACHE = 2

class Dictionary:
    def __init__(self, cache_capacity=10):
        self.local_dict = LocalDictionary()
        self.cache = LruCache(cache_capacity)

    def search(self, word):
        dummy_entry = DictionaryEntry(word, '', '')
        try:
            entry = self.cache.search(dummy_entry)
            return (entry, DictionarySource.CACHE)
        except KeyError:
            entry = self.local_dict.search(word)
            self.cache.add(entry)
            return (entry, DictionarySource.LOCAL)

def main():
    dictionary = Dictionary(cache_capacity=1)
    while True:
        word = input("Enter a word to lookup: ").strip()
        if not word:
            continue
        try:
            entry, source = dictionary.search(word)
            print(entry)
            print(f"(Found in {source.name})")
        except KeyError as e:
            print(f"Error when searching: {e}")

if __name__ == "__main__":
    main()