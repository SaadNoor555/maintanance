import re
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

def newline_remover(text):
    code_lines = []
    lines = text.split('\n')
    for line in lines:
        if line=='' or line.isspace():
            continue
        else:
            code_lines.append(line)
    return '\n'.join(code_lines)

def count_lines(text):
    return len(text.split('\n'))

def process(code):
    return count_lines(newline_remover(comment_remover(code)))


if __name__ == "__main__":
    filename = 'fib.cpp'
    file = open(filename)
    text = file.read()
    print(process(text))