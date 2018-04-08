FanXchange Technical
===

The Challenge:
Create a simple application that takes a UTF-8 plain-text file as input and outputs:
- The total number of words in the text file.
- The ten most common words and number of occurrences for each.

Usage
===

``` python ./word_counter.py [example.txt]```

where example.txt is the file you want to run the program on

### wordCount
returns a integer representing the number of words in the .txt file

### mostCommonWords
returns a dict of the (default 10) most common words in the .txt file. I had the function return a dict over a list since key value pairs are more robust over tuple pairs and hardcode list stirngs.

Testing
===
To run the testing suite

```python ./test.py```
