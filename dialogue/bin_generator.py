from dialogue.extractor import DialogueExtractor

import os
from shutil import rmtree
import glob

class DialogueBinGenerator:
    def __init__(self, json_dir, bin_dir):
        self.json_dir = json_dir
        self.bin_dir = bin_dir

    def generate(self):
        if os.path.exists(self.bin_dir):
            rmtree(self.bin_dir)
        os.mkdir(self.bin_dir)

        for file in glob.iglob(f'{self.json_dir}/*.json'):
            extractor = DialogueExtractor(file)
            extractor.extract(self.bin_dir)
