from prompt_generator import PromptGenerator

SCN_DIR = 'scn_files'
TEMP_DIR = 'temp'
PROMPT_OUTPUT_DIR = 'output'

generator = PromptGenerator(SCN_DIR, TEMP_DIR, PROMPT_OUTPUT_DIR)
generator.generate()
