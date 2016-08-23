import os

def get_migrations_filenames(dirname):
	files = os.listdir(dirname)
	files = filter(lambda x: x.endswith("sql"), files)
	files = [file.split(".")[0] for file in files]
	return sorted(files)