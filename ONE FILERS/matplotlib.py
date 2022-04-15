import matplotlib.pyplot as pyplot

# # A LOT OF HELP INFO:
# help(pyplot.plot)
# https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/

# # Basic example
# pyplot.plot([2, 4, 1, 6])
# pyplot.ylabel('Random numbers')
# pyplot.subtitle('Basic example', fontsize=20)
# pyplot.title('Subtitle', fontsize=10)
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

# Remove labels
# Note that "ticks" refer to the actual lines and values, but the "label" refers to the axis title like "Days in use" or whatever
# ax = pyplot.gca()
# ax.axes.xaxis.set_visible(False) # This will hide both labels and ticks
# ax.axes.xaxis.set_ticklabels([]) # This will remove the values but keep the tick lines
# pyplot.tick_params(left = False, bottom = False) # This will remove the ticks and values, but keep the label