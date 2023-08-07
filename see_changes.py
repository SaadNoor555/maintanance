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

  with open(output_file, "a") as f:
    f.writelines([old_file])
    f.writelines(diff)


if __name__ == "__main__":
  old_file = "fib.cpp"
  new_file = "fin_1.cpp"
  output_file = "fib.diff"

  write_changes(old_file, new_file, output_file)