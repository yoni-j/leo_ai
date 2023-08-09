import itertools
import os

import pandas as pd


class FrequencyService:
    TABLE_SIZE = 5

    def __init__(self):
        self.frequency_list = {}

    # Clears text from non alphabet characters, casing and stop words
    @staticmethod
    def process_text(text: str) -> str:
        text = text.lower()
        text = ''.join(c for c in text if c.isalpha() or c.isspace())
        words = text.split()
        stop_words = {"to", "and", "the", "of", "in", "a"}
        filtered_words = [word for word in words if word not in stop_words]
        processed_text = ' '.join(filtered_words)

        return processed_text

    def find_frequency_in_text(self, text: str):
        text = self.process_text(text)
        words_list = text.split()
        for word in words_list:
            new_count = self.frequency_list.get(word, 0) + 1
            self.frequency_list[word] = new_count

    def collect_frequency_from_paths(self, paths: list[str]):
        for text_file in paths:
            with open(os.getcwd()+text_file) as f:
                content = f.read()
                self.find_frequency_in_text(content)

    def print_table(self):
        data_list = [(word, frequency) for word, frequency in self.frequency_list.items()]
        df = pd.DataFrame(data_list, columns=['word', 'frequency'])
        df_sorted = df.sort_values(by='frequency', ascending=False)
        top_5 = df_sorted.head(self.TABLE_SIZE)
        print(top_5.to_string(index=False))
