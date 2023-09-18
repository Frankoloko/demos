def what_is_this(name, variable):
    """Some summary line.

    This function will print a lot of details of any variable. Very useful to
    figure out what keys, functions, types etc something is.

    Args:
        name (str): The name of your variable like "x"
        variable (anything): Anything you want
    """
    print('-'*20)
    print('WHAT IS: {}'.format(name))
    print('\n')
    
    print('type()', type(variable))
    print('\n')

    print('dir()', dir(variable))
    print('\n')

    try:
        print('keys()', variable.keys())
    except AttributeError:
        print('keys()', 'None')

    print('='*20)