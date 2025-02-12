def main():

    in_file = open('word_count.txt')
    lines = in_file.read().split("\n")
    line_count = len(lines)
    word_count = 0
    char_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
        char_count += len(line)
    print("File has {0} lines, {1} words, {2} charcters".format(line_count, word_count, char_count))

    r = 1
    n = 5
    while n > 0:
        r = r * n
        n = n - 1
    print(r)

if __name__ == '__main__':
    main()