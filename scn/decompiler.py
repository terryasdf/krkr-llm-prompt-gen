import os
import glob
from subprocess import Popen, PIPE

PSB_DECOMPILE_PATH = 'FreeMoteToolkit/PsbDecompile'

class SCNDecompiler:

    def __init__(self, scn_dir, raw_json_dir):
        self.scn_dir = scn_dir
        self.raw_json_dir = raw_json_dir

    def decompile_scn(self):
        if not os.path.exists(self.raw_json_dir):
            os.mkdir(self.raw_json_dir)

        processes = [
            Popen([PSB_DECOMPILE_PATH, file], stdout=PIPE) for file in glob.iglob(f'{self.scn_dir}/*.scn')
        ]
        return [p.wait() for p in processes]
