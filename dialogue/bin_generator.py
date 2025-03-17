from dialogue.extractor import DialogueExtractor

import os
from shutil import rmtree
import glob

class DialogueBinGenerator:
    def __init__(self, json_dir, dst_dir):
        self.json_dir = json_dir
        self.dst_dir = dst_dir

    def generate(self):
        if os.path.exists(self.dst_dir):
            rmtree(self.dst_dir)
        os.mkdir(self.dst_dir)

        for file in glob.iglob(f'{self.json_dir}/*.resx.json'):
            os.remove(file)
        for file in glob.iglob(f'{self.json_dir}/*.json'):
            dst = f'{self.dst_dir}/{os.path.split(file)[-1]}'
            if os.path.exists(dst):
                os.remove(dst)
            os.rename(file, dst)

            extractor = DialogueExtractor(dst)
            extractor.extract()
