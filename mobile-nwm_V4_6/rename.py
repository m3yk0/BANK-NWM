from os import path, renames, getcwd, walk
replac = input(f"nome que deseja retirar de todas as pastas e arquivos: ")
lispath = path.abspath(path.expanduser(path.expandvars(getcwd())))
print('\n', lispath)
for a,b, files in walk(lispath):
	print(f"{a=}\n{b=}\n{files=}\n")
	for file in files:
		new = file.strip().replace(replac, '').strip()
		renames(file, new)
		print(file, '  >>>>>>  ', new)