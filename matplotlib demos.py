import matplotlib.pyplot as pyplot

# # A LOT OF HELP INFO:
# help(pyplot.plot)
# https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/

# # Basic example
# pyplot.plot([2, 4, 1, 6])
# pyplot.ylabel('Random numbers')
# pyplot.title('Basic example')
# pyplot.figure(figsize=(10,7)) # Set graph size, 10 is width, 7 is height
# pyplot.show()

# # X/Y example
# pyplot.plot(
#     [2, 4, 6, 8], # x
#     [4, 8, 12, 16] # y
# )
# pyplot.ylabel('Double X')
# pyplot.xlabel('X values')
# pyplot.show()

# # Graph style formats
# pyplot.plot(
#     [2, 4, 6, 8], # x
#     [4, 8, 12, 16], # y
#     'bD-.' # Plotting formats:
#             # go- = GREEN-DOTS-LINE
#             # r*-- = RED-STAR-DASHED_LINE
#             # ks. = BLACK-SQUARES-DOTTED_LINE
#             # bD-. = BLUE-DIAMOND-DASH_DOT_LINE
# )
# pyplot.ylabel('Double X')
# pyplot.xlabel('X values')
# pyplot.show()

# # Two sets of plots
# pyplot.plot([1,2,3,4,5], [1,2,3,4,10], label='Bottom set')
# pyplot.plot([1,2,3,4,5], [2,3,4,5,11], label='Top set')
# pyplot.legend(loc='best')
# pyplot.show()