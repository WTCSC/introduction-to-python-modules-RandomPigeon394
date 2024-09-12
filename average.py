import text_utils
"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""
def line_count():
  counter = 0
  total_words = 0
  file = open('sample.txt', 'r')
  lines = file.readlines()
  for line in lines: 
      counter = counter + 1
      total_words = total_words + (text_utils.count_words(line))
      
  file.close()
  return total_words // counter
print(f"Average words per line: {line_count()}")