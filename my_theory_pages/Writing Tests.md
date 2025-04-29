# Why writes tests

Why even write tests in the first place? If you tested your code works, then it works, why care about writing a test to verify what you already verified?

A few main reasons:
- `Save time` A computer can test thousands of tests in a milisecond, a dev can not.
- `Find bugs` You can never test enough. Because any time you dissapoint a client with broken code, is one dissapointment too many.
- `Teams` Devs who work in teams, are changing different pieces of the codebase all the time. It is hard to know if a change in one location would break something written in another location. An automated test is an easy way to test that your small change did not break things you weren't aware of.
- `To simplify the code` The fundamental reason why this document was written in the first please. Read on. 
- `Test multiple platforms` You can write a test once, and then test it on Windows & Linux & Mac runners automatically.

# Unit vs Integration Meanings

The first point to understand about tests is that you have two main types (there are more, but these two are really fundamental).

- `Unit` Test the small pieces separately
- `Integration` Test that all the small pieces work when put together.

You should generally have more Unit tests than Integration tests. If you look up the most common testing pyramids, the Unit tests are at the bottom. And the bottom of the pyramid has more volume than the top. The reason for this is simple. If units are thoroughly tested, most integrations are more likely to work, but integration tests are critical because unit tests cannot guarantee correct collaboration between units. But in general, you should have more Units tests than Integration tests.

# Unit vs Integration is a question of Perspective

Now, understand that in every single example, you can zoom in or out to see something as a Unit or Integration test. Knowing whether something is a Unit or Integration test, is merely a matter of perspective.

- For a website, the HTML login screen is the Integration, while the `login()` API doing the login is the Unit.
- For a login API, the `login()` function is the Integration, while the `verify_user()` and `create_api_token()` are Units.
- For the verify user module, the `verify_user()` is the Integration, while the `connect_to_database()` and `check_user_permissions()` are Units.

You see the point here, anything can be a Unit or Integration test, it just depends how deep you want to zoom.

# Incorrect Example

Now let's look at some practical examples. Here is very valid function. There is technically nothing wrong with it. It would be accepted just fine in most teams.

```python
def process_data(data):
    # Step 1: Validate data
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")
    if not all(isinstance(item, int) for item in data):
        raise ValueError("All elements in the list must be integers")

    # Step 2: Filter negative numbers
    filtered_data = [item for item in data if item >= 0]

    # Step 3: Compute statistics
    total = sum(filtered_data)
    count = len(filtered_data)
    average = total / count if count > 0 else 0

    return total, count, average
```

Writing a test for this would now be simple.

```python
def tests():
    process_data([1, -3, 2, 3]) == 6, 3, 2
```

# Correct Example

But see how it can be better if you think more in the line of `how can I test this easier`.

```python
def _validate_data(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")
    if not all(isinstance(item, int) for item in data):
        raise ValueError("All elements in the list must be integers")

def _filter_negative_numbers(data):
    return [item for item in data if item >= 0]

def _compute_statistics(data):
    total = sum(data)
    count = len(data)
    average = total / count if count > 0 else 0
    return total, count, average

def process_data(data):
    _validate_data(data)
    filtered_data = _filter_negative_numbers(data)
    total, count, average = _compute_statistics(filtered_data)
    return total, count, average
```

Now we can test the Units more easily.

```python
def tests():
    # Unit tests
    _validate_data([1, "wrong", 2, 3]) == raises ValueError("All elements in the list must be integers")
    _filter_negative_numbers([1, -3, 2, 3]) == [1, 2, 3]
    _compute_statistics([1, 2, 3]) == 6, 3, 2

    # Integration test
    process_data([1, -3, 2, 3]) == 6, 3, 2
```

Due to the mindset of thinking about your tests, you have now created better code. The code is now easier to understand, easier to test, easier to replace certain parts, easier to expand with new functionality, easier to reuse elsewhere...the list keeps going.

# The client pays you for code, not tests

True. But that's like saying a you get paid to build a house, not to build a house correctly. When building a house, the client assumes you are building a house according to the correct standards. If they want a cheaper job, and a worse quality house, they can hire a cheaper builder.

Code + tests is good code. Code without tests is cheap code.

A coder with tests will have the client for a lifetime. A coder without tests will get fired when the client is completely fed up with broken changes. And/or every feature will get harder and harder to implementment.

# You can waste time

Sure, you can waste time writing too many tests. So be careful to not overdo it. Just like you can overengineer a bridge.

But saying that any test is a waste of time, is wrong. That would be like building a bridge without testing anything beforehand. Sure it might work, but it might also just collapse or constantly break and need fixing.

# `Good tests find mistakes. Great tests simplify code.`