import sys, fileinput, re, nltk
from nltk.tokenize import sent_tokenize


def main():
    for line in fileinput.input():
        if line.strip() != "":
            line = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', line.strip())

            sentences = sent_tokenize(line.strip())

            for s in sentences:
                if s != "":
                    sys.stdout.write(s + "\n")

if __name__ == "__main__":
    main()