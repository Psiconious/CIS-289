"""
Name: Trever Cluney
Date: 01.31.22
Email: tlcluney@dmacc.edu
Overview: counting the number of times a word appears in the 2 passages and checking average length of a sentence
"""
import re


def file_word_count(file):
    """Edited version of the moby dick example file to be generic."""
    input_file_word_count = {}
    with open(file, 'r') as input_file:
        for line in input_file:
            # First lowercase all characters in the line
            line = line.lower()
            # Next clean the line of any punctuation
            line_clean = re.sub(r'[^\w\s]', '', line)
            # Now split the line into words
            line_split = line_clean.split()
            # Now we can add the words to our dictionary
            for word in line_split:
                if word in input_file_word_count.keys():
                    input_file_word_count[word] += 1
                else:
                    input_file_word_count[word] = 1
        return input_file_word_count


def average_sentence_length(file):
    """Counts the amount of characters in a sentence. Doesn't account for non-period ends or if its a title"""
    average_length = 0
    with open(file, 'r') as input_file:
        content = input_file.read()
    content = content.replace('\n', '')
    sentences = content.split('.')
    sentences = list(map(str.strip, sentences))

    for sentence in sentences:
        if len(sentence) > 0:
            average_length += len(sentence)
    average_length /= len(sentences)
    return round(average_length)
    pass


if __name__ == '__main__':
    moby_dick_word_count = file_word_count('Moby_Dick_Chapter_1.txt')
    sense_and_sensibility_word_count = file_word_count("Sense_and_Sensibility_Chapter_1.txt")
    try:
        mb_old_count = moby_dick_word_count['old']
    except:
        mb_old_count = 0
    try:
        mb_water_count = moby_dick_word_count['water']
    except:
        mb_water_count = 0
    try:
        ss_old_count = sense_and_sensibility_word_count['old']
    except:
        ss_old_count = 0
    try:
        ss_water_count = sense_and_sensibility_word_count['water']
    except:
        ss_water_count = 0
    print('Times the word old appear in Moby Dick: {}'.format(mb_old_count))
    print('Times the word old appear in Sense and Sensibility: {}'.format(ss_old_count))
    print('Times the word water appear in Moby Dick: {}'.format(mb_water_count))
    print('Times the word water appear in Sense and Sensibility: {}'.format(ss_water_count))
    mb_avg = average_sentence_length('Moby_Dick_Chapter_1.txt')
    ss_avg = average_sentence_length('Sense_and_Sensibility_Chapter_1.txt')
    print('Average sentence length for Moby Dick: {}'.format(mb_avg))
    print('Average sentence length for Sense and Sensibility: {}'.format(ss_avg))
