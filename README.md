# thinking-functional-python

[![Build Status](https://travis-ci.org/sammyrulez/thinking-functional-python.svg?branch=master)](https://travis-ci.org/sammyrulez/thinking-functional-python)

A collection of functional programming recipes in python.

Quotes from [Thinking Functional](http://shop.oreilly.com/product/0636920029687.do) 

## Chapter 1

>Read a file of text, determine the most
>frequently used words, and print out a sorted list of those words along with their frequencies

Using just what the standard library has to offer the problem can be solved like this:

```python
map(populate_freq, filter(lambda w: w not in NON_WORDS,map(lower_f, re.findall('\w+', words))))

```

IMHO this is not really readable code and is against the Zen of python

>Explicit is better than implicit.
>Simple is better than complex.

The main problem here is that what happens first is at the end of the expression. A tail style would be more readable:

```python
re.findall('\w+', words).map(lower_f).filter(lambda w: w not in NON_WORDS).iterate(populate_freq)

```

To do so an additional data structure is required: the [FunList](https://github.com/sammyrulez/thinking-functional-python/blob/master/chp1/word_frequencies.py#L8-L8). It is an iterable with methods that apply on its 
own content and return a new instance in order to preserve immutability


>For each of the searchChars, find the index
>of the first encountered match within the target string

In this case there is no way to avoid a nested loop

```python
def first_index_of(string,chars):

    def lazy_index_generator():
        for pair in zip(range(0,len(string)),string):
            for c in chars:
                if c == pair[1]:
                    yield pair[0]


    return first(lazy_index_generator())

```

But this function has no side effects, is easy to understand and the generator allow the best performance since 
it is executed only the exact number of times needed to reach the first match. 
