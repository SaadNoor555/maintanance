import filecmp
import difflib

def write_changes(old_file, new_file, output_file):
	"""Writes the changes between the old and new files to the output file."""
	# print('yo')
	with open(old_file, "r") as f:
		old_lines = f.readlines()

	with open(new_file, "r") as f:
		new_lines = f.readlines()

	diff = difflib.unified_diff(old_lines, new_lines, "old", "new", lineterm="")
	added, deleted, total = 0, 0, 0
	for dif in diff:
		if dif!= '--- old' and dif!='+++ new' and dif[:2]!='@@':
			# print(dif)
			if dif[0]=='+': added += 1
			if dif[0]=='-': deleted += 1
	total = added+deleted
	# print(added, deleted, total)
	with open(output_file, 'a') as f:
		f.write(old_file+'\n')
		f.writelines(['added: '+str(added)+'\n', 'deleted: '+str(deleted)+'\n', 'total: '+str(total)+'\n'])
		f.write('----------------------------------\n')
	


if __name__ == "__main__":
  old_file = "fib.cpp"
  new_file = "fin_1.cpp"
  output_file = "sha.diff"

  write_changes(old_file, new_file, output_file)