import os
import glob
from shutil import rmtree
from subprocess import Popen, PIPE

PSB_DECOMPILE_PATH = 'FreeMoteToolkit/PsbDecompile'

class SCNDecompiler:

    def __init__(self, scn_dir, json_dir):
        self.scn_dir = scn_dir
        self.json_dir = json_dir

    def decompile_scn(self):
        if os.path.exists(self.json_dir):
            rmtree(self.json_dir)
        os.mkdir(self.json_dir)

        processes = [
            Popen([PSB_DECOMPILE_PATH, file], stdout=PIPE) for file in glob.iglob(f'{self.scn_dir}/*.scn')
        ]
        _ = [p.wait() for p in processes]
    
        for file in glob.iglob(f'{self.scn_dir}/*.resx.json'):
            os.remove(file)

        for file in glob.iglob(f'{self.scn_dir}/*.json'):
            dst = f'{self.json_dir}/{os.path.split(file)[-1]}'
            if os.path.exists(dst):
                os.remove(dst)
            os.rename(file, dst)
