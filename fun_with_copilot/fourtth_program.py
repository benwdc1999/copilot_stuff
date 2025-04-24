def longest_word(words):
   """ Words is a list of words
   
   Return the word from the list with the most characters.
   If multiple words are the longest, return the first such word.

   >>> longest_word(['cat', 'dog', 'bird'])
   'bird'

    >>> longest_word(['happy', 'birthday', 'my', 'cat'])
    'birthday'

    >>> longest_word(['happy'])
    'happy'

    >>> longest_word(['cat', 'dog', 'me'])
    'cat'

    >>> longest_word([','])
    ','

   """
   longest = ""
   for i in range(0, len(words)):
         if len(words[i]) >= len(longest):
              longest = words[i]
   return longest

import doctest
doctest.testmod()

