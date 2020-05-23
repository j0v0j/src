import glob
class Filelist():
    def  __init__(self,filetype):
        self.filetype=filetype
    def listfile(self):
        #recursive=True 不断进入文件夹遍历
        filelist = glob.glob(r"*/*."+self.filetype, recursive=False)
        return filelist

