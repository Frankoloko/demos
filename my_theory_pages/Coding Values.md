# Summary

* Make it importable
* Understandability over performance
* Comment well

# Make it importable and testable

* Make it "importable". In Python, you should be able to import just this single function and test it's outcome. This "importable" mindset is one of the greatest ways of simplifying your code.
* Break code into the smallest possible parts. Smaller components are easier to test, replace, and improve over time.
* Think of it like building a car engine, not from a single massive steel block, but from modular, interchangeable, testable parts. Core engineering principles favor small, testable units.
* Put GREAT CARE into simplifying the inputs to functions! A big problem with modular functions is that their inputs are complex objects. Therefore you are required to run everything anyways, because you cannot simply recreate the input yourself.
* If done well, this mindset also improves your automated testing. Because when functions are simple, they are easy to write tests for.

# Understandability over performance

* In Pipeline (specifically in Pipeline!) performance is not the top priority. Clarity and readability should take precedence.
* Readable code makes it easier for newcomers to learn, reduces confusion, and minimizes the likelihood of bugs caused by misinterpretation.
* Other domains like gaming requires a lot more care on performance, but not Pipeline.

# Comment a lot

* Comments make it easier and faster to understand the code, reducing the risk of misinterpretation and bug creation.
* The cost to benefit ratio of comments highly outweights the beneficial side. So when in doubt, just leave a comment.
* Comments are capable of simplifying immensely complex blocks of logic. A single comment can make an entire section make more sense.
* We are humans, we need consume information better when it is written in a language you understand. English is much easier to understand than Python.
* Obiviously, don't overdo comments. Not every line needs a comment. But most people underdo comments anyways, so you should be fine.

# Pass strings, not objects

* Reason: strings are easier to test

* Passing objects definitely gives you faster code. But objects can be really hard to test sometimes.

For example, which of these two functions would you be able to debug easier?

1. test_strings("hi", "there", "dude")
2. test_strings(Str, Str, Str)

That is a simple example, but now replace those with more custom classes and you'll quickly see that the incomming objects are as much an obstacle to the debugging than the function it self.

