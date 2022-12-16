import sys
script, input_encoding, errors = sys.argv

def main(language_file, line, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encoding(encoding, errors=errors)
    cooked_strings = raw_bytes.decode(encoding,errors=errors)

    print(raw_bytes + " <===> " + cooked_strings)


languages = open("languages.txt", encoding="utf-8") 


main(languages, input_encoding, error)