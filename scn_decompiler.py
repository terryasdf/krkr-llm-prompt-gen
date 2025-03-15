import os
import glob
from subprocess import Popen, PIPE

PSB_DECOMPILE_PATH = 'FreeMoteToolkit/PsbDecompile'
RAW_JSON_PATH = 'temp'

class SCNDecompiler:

    def __init__(self, scn_folder: str):
        self.scn_folder = scn_folder

    def decompile_scn(self):
        if not os.path.exists(RAW_JSON_PATH):
            os.mkdir(RAW_JSON_PATH)

        processes = [
            Popen([PSB_DECOMPILE_PATH, f], stdout=PIPE) for f in glob.iglob(f'{self.scn_folder}/*.scn')
        ]
        _ = [p.wait() for p in processes]
        print('==========SCN DECOMPILATION DONE===========')
        for f in glob.iglob(f'{self.scn_folder}/*.resx.json'):
            os.remove(f)
        for f in glob.iglob(f'{self.scn_folder}/*.json'):
            dst = f'{RAW_JSON_PATH}/{os.path.split(f)[-1]}'
            if os.path.exists(dst):
                os.remove(dst)
            os.rename(f, dst)