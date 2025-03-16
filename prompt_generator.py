from scn.decompiler import SCNDecompiler
from dialogue.bin_generator import DialogueBinGenerator

class PromptGenerator:
    def __init__(self, scn_dir, temp_dir, output_dir):
        self.decompiler = SCNDecompiler(scn_dir, temp_dir)
        self.bin_generator = DialogueBinGenerator(scn_dir, temp_dir)

    def generate(self):
        self.decompiler.decompile_scn()
        print('==========SCN DECOMPILATION DONE===========')
        self.bin_generator.generate()
        print('==========DIALOGUE BIN CREATED===========')
