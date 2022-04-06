import re
moby_dick_word_count = {}

with open('Moby_Dick_Chapter_1.txt', 'r') as input_file:
    for line in input_file:
        # First lowercase all characters in the line
        line = line.lower()
        # Next clean the line of any punctuation
        line_clean = re.sub(r'[^\w\s]', '', line)
        # Now split the line into words
        line_split = line_clean.split()
        # Now we can add the words to our dictionary
        for word in line_split:
            if word in moby_dick_word_count.keys():
                moby_dick_word_count[word] += 1
            else:
                moby_dick_word_count[word] = 1

data_for_output = sorted(moby_dick_word_count.items(), key=lambda x: x[1], reverse=True)

with open("moby_dick_word_counts.txt",'w') as fileoutput:
    for item in data_for_output:
        fileoutput.write(item[0] + " " + str(item[1])+ "\n")

for word in moby_dick_word_count:
    print("Word: {}, Count: {}".format(word, moby_dick_word_count[word]))
