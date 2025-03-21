from scn.decompiler import SCNDecompiler
from dialogue.bin_generator import DialogueBinGenerator
from dataset.text_collector import PromptTextCollector

class DatasetGenerator:
    def __init__(self, scn_dir, temp_dir, output_dir):
        bin_dir = f'{temp_dir}/bin'
        self.decompiler = SCNDecompiler(scn_dir, temp_dir)
        self.bin_generator = DialogueBinGenerator(temp_dir, bin_dir)
        self.text_processor = PromptTextCollector(bin_dir, output_dir)

    def generate(self):
        self.decompiler.decompile_scn()
        print('==========SCN DECOMPILATION DONE===========')
        self.bin_generator.generate()
        print('==========DIALOGUE BIN CREATED===========')
        self.text_processor.process()
        print('==========PROMPT CSV GENERATED===========')
