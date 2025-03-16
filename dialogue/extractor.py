import json
import pickle
from os.path import abspath

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

        scenes = data['scenes']
        lines = []
        for scene in scenes:
            if 'texts' not in scene:
                continue

            texts_opt_list = scene['texts']
            for opt in texts_opt_list:
                role = opt[0]
                # Main character thinking, no one speaking
                if not role:
                    continue

                # opt[1][i][0] -> displayed character name (might not be identical with the real one)
                # opt[1][i][1] -> displayed text
                # opt[1][i][2] -> char count

                texts = [lang[1] for lang in opt[1]]
                lines.append((role, texts))

            with open(f"{self.path}.bin", "wb") as f:
                pickle.dump(lines, f)
                print(f'Successfully saved pickled dialogues: {abspath(f.name)}')
