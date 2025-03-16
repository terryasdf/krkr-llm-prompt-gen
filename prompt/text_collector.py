import os
import glob
import pickle
import csv

from prompt.text_preprocessor import preprocess_text

class PromptTextCollector:

    def __init__(self, bin_dir, output_dir):
        self.bin_dir = bin_dir
        self.output_dir = output_dir

    def process(self):
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

        with open(f'{self.output_dir}/prompts.csv', 'w', encoding='utf-8') as fw:
            csvwriter = csv.writer(fw)
            for file in glob.iglob(f'{self.bin_dir}/*.bin'):
                with open(file, 'rb') as fr:
                    lines = pickle.load(fr)

                if not len(lines):
                    print(f'**Empty bin: {os.path.split(file)[-1]}**')
                    continue

                NUM_LANG = len(lines[0][1])
                last_role = None
                concat = [''] * NUM_LANG
                for role, text in lines:
                    assert role
                    if role != last_role:
                        csvwriter.writerow([last_role] + concat)
                        last_role = role
                        concat = [''] * NUM_LANG
                    for i in range(NUM_LANG):
                        concat[i] += preprocess_text(text[i])
                if len(concat[0]):
                    csvwriter.writerow([last_role] + concat)
