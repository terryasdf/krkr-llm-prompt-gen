import json
import pickle
from os.path import abspath

END_MARK = '<END>'

def get_stage(opt):
    for o in opt[4]['data']:
        if o[0] == 'stage':
            return o[2]['redraw']['imageFile']['file']
    return None

class DialogueExtractor:
    """
    Extracts dialogues from decompiled scn and save into pickle files.
    """

    def __init__(self, path):
        self.path = path

    def extract(self):
        """
        Returns a list of tuples, the first element of which is the character and
        second is a list of corresponding dialogues in all languages.
        """

        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        num_lang = -1
        scenes = data['scenes']
        lines = []
        try:
            for scene in scenes:
                if 'texts' not in scene:
                    continue

                texts_opt_list = scene['texts']
                assert len(texts_opt_list)
                last_stage = get_stage(texts_opt_list[0])

                if num_lang >= 0 and len(texts_opt_list[0][1]) != num_lang:
                    raise IndexError()
                num_lang = len(texts_opt_list[0][1])
                END_LINE = (END_MARK, [''] * num_lang)

                try:
                    for opt in texts_opt_list:
                        role = opt[0]

                        stage = get_stage(opt)
                        if last_stage != stage:
                            lines.append(END_LINE)
                            last_stage = stage

                        # Main character thinking, no one speaking
                        if not role:
                            if len(lines) and lines[-1][0] != END_MARK:
                                lines.append(END_LINE)
                            continue


                        # opt[1][i][0] -> displayed character name (might not be identical with the real one)
                        # opt[1][i][1] -> displayed text
                        # opt[1][i][2] -> char count

                        texts = [lang[1] for lang in opt[1]]
                        if len(opt[1]) != num_lang:
                            raise IndexError()

                        lines.append((role, texts))

                except IndexError:
                    print(f'Found language number mismatch in:\n\t{texts}\nSkipping current scene')
        except IndexError:
            print(f'Found language number mismatch in file:\n\t{self.path}Skipping current file')

        with open(f'{self.path}.bin', 'wb') as f:
            pickle.dump(lines, f)
            print(f'Successfully saved pickled dialogues: {abspath(f.name)}')
