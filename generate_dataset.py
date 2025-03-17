from dataset.generator import DatasetGenerator

SCN_DIR = 'scn_files'
TEMP_DIR = 'temp'
PROMPT_OUTPUT_DIR = 'output'

generator = DatasetGenerator(SCN_DIR, TEMP_DIR, PROMPT_OUTPUT_DIR)
generator.generate()
