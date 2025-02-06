from pathlib import Path


path_atual = Path()

files = path_atual / 'files'

absoluto = files.absolute() # PosixPath('/home/gui/notebook_repo/files')

files.name # 'files'
absoluto.root # '/'

absoluto.parent # PosixPath('/home/gui/notebook_repo')

absoluto.parts # ('/', 'home', 'gui', 'notebook_repo', 'files')