# Summary

* Make it as small as possible
* Understandability over performance
* Comment well

# Make it as small as possible

Make the parts as small as possible. Small parts are more easily tested and replaced by better parts in the future.

The same reason you don't build a car engine from one massive steel block. A core engineering principle is to make things small and easily testable.

Another important point here, is to make the inputs as simple as possible. There is no use in splitting out a function for easy testing, but the inputs to that function are really hard to recreate without running through the entire system.

Making things smaller also makes it easier to understand. It's easier to understand what many small components do, than to understand an entire machine without looking at the smaller parts. The concept of "car" is unimaginably complex, but a "fuel pump" + "piston" is very easy to understand.

# Understandability over performance

In Pipeline (specifically in Pipeline!) performance is not a very important factor. Therefore, weight the scale more towards making code understandable. Making code more understandable will make it easier for newcomers to learn and less likely to cause problems because of confusion.

# Comment well

It is important to note big blocks of logic with human words. Therefore making it easier and faster to understand. While also lowering the chance of confusion that could lead to problems.

Too much commenting is better than too little commenting.

# Thing API + UI

In almost all cases, you should be thinking of code as an API speaking to a UI. In other words, a caller(the UI) and an executor(the API).

You should imagine that you can test every piece of code by running the basic command in a terminal. If you can't do that, then you probably haven't broken down the code enough to test the smaller pieces.

Also, whenever you have a real UI involved. Almost all the logic functions of the UI, should be runnable in API form. Basically, the UI should just be connecting and running many API functions. But never really building up it's own new functions.