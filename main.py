# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# def read_file_content(filename):
# [assignment] Add your code here
with open("Reading-Text-Files\story_1.txt") as f:
    contents = f.read()
    print(contents)
 #   return "Hello World"


# def count_words():
   # text = read_file_content("./story.txt")
    # [assignment] Add your code here
file = open("Reading-Text-Files\story.txt", "r")
read_data = file.read()
word_count = read_data.count("as")
print('"as"'' :', word_count)

word_count = read_data.count("would")
print('"would"'' :', word_count)
# return {"as": 10, "would": 20}
