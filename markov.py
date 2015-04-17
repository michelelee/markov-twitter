import sys
from random import choice


def make_chains(input_text):
    """Takes input text as string; returns dictionary of markov chains."""
    # input_text is a whole text file with lines
    # input_text.read() ??
    # input_text_in_list = input_text.split(" ")
    content_list = input_text.read().split()
    # content_list = [w.rstrip("?.,\n") for w in content_list]
    bigram_dict = {}
    
    for index in range(len(content_list) - 2):
        bigram_key = (content_list[index], content_list[index + 1])
        word_after_bigram_key = content_list[index + 2]

        if bigram_key not in bigram_dict:
            bigram_dict[bigram_key] = []
      
        bigram_dict[bigram_key].append(word_after_bigram_key)
        # list.append(value)


    # the new list created from words in input_text should be stored to a new variable
    return bigram_dict

    
def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    # chains is the dictionary
    # we have bigram_dict, its in chain
    # now lets make a string...
    # string of random... key 1 + random.choice(value_list) + key 2 + random.choice...
    

    # How long do we go? until we cannot find the key!
    words = []
    random_key = choice(chains.keys())
    words.append(random_key[0])
    words.append(random_key[1])

    # random text now equals "would you"
    # can we find...value like bigrams_dictionary['would you'] = [list of words]

    while random_key in chains:
        # # key is a tuple
        next_word = choice(chains[random_key])

        words.append(next_word)
        # first key should added to the string when it is used the first time... or selected 
        # then the 3 words... will continually be joined 
        # this will print the key every time it loops over, we only need it the first time. 

        # new random_key
        random_key = (random_key[1], next_word)

    words_string = " ".join(words)
    
    print words_string



# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

#######################################################
# input_text = "Some text"
flower = open(sys.argv[1])
# # Get a Markov chain
chain_dict = make_chains(flower)
# hain_dict = bigram_dict

# Produce random text
random_text = make_text(chain_dict)

print random_text


# make_chains(x)

# input_text= """Hello this is natalie and mish.
# We are in class. 
# It is super hot today.
# I want air conditioning. """

