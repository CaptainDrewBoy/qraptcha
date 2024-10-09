# Returns tuple containing string with asterixed words removed and word within asterixes
def remove_asterixed(string):
    word_array = string.split()
    for i in range(len(word_array)):
        if word_array[i][0] == "*":
            removed_word = word_array[i].strip("*")
            word_array[i] = "_"
    return (" ".join(word_array), removed_word)

def main():
    with open("quotes.txt") as file:
        for line in file:
            line = line.strip("\n")
            my_tuple = remove_asterixed(line)
            print(f"{line} -> {my_tuple[0]} (removed {my_tuple[1]})")

if __name__ == "__main__":
    main()
