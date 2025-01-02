# Making the Case for Tuples
# When most programmers new to Python first come across the tuple, they question why such a data structure even exists. 
# After all, a tuple is like a list
# that cannot be changed once it’s created (and populated with data). Tuples are immutable: they cannot change. So, why do we need them?
# It turns out that having an immutable data structure can often be useful. Imagine that you need to guard against side effects by ensuring some data
# in your program never changes. Or perhaps you have a large constant list (which you know won’t change) and you’re worried about performance.
# Why incur the cost of all that extra (mutable) list processing code if you’re never going to need it? Using a tuple in these cases avoids unnecessary
# overhead and guards against nasty data side effects (were they to occur).

vowels = ('a', 'e', 'i', 'o', 'u')

# Watch Out for Single-Object Tuples
# Let’s imagine you want to store a single string in a tuple. It’s tempting to put the string inside parentheses, and then assign it to a variable name...but doing
# so does not produce the expected outcome. Take a look at this interaction with the >>> prompt, which demonstrates
# what happens when you do this:

t = ('Python')
print(type(t))
print(t)

# What looks like a single-object tuple isn’t; it’s a string. This has happened due to a syntactical quirk in the Python language. The rule is that, in order
# for a tuple to be a tuple, every tuple needs to include at least one comma between the parentheses, even when the tuple contains a single object. 
# This rule means that in order to assign a single object to a tuple (we’re assigning a string object in this instance), 
# we need to include the trailing comma, like so:


t2 = ('Python',)
print(type(t2))
print(t2)