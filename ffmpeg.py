# Good resources
# https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730

import subprocess

ffmpeg = '\\\\reef\\Pipeline\\tf_global\\shared\\libraries\\ffmpeg\\ffmpeg-n4.4-78-g031c0cb0b4-win64-gpl-4.4\\bin\\ffmpeg.exe'
source = 'C:\\Users\\francois.kruger\\Documents\\tf_global\\dev\\tf_ffmpeg\\test.mp4'
output = 'C:\\Users\\francois.kruger\\Documents\\tf_global\\dev\\tf_ffmpeg\\output.mp4'

##########################################

# Basic input and output of video file
# command = '{ffmpeg} -i {input} -y {output}'.format(ffmpeg=ffmpeg, input=source, output=output)

# Change the video's timecode (starting point). Remember, you'll only see this change in advanced software like RV.
# command = '{ffmpeg} -i {input} -timecode 10:00:00:00 -y {output}'.format(ffmpeg=ffmpeg, input=source, output=output)

# Add text to video
# text_line = "drawtext=fontfile=/Windows/fonts/calibri.ttf:text='Test Text':fontcolor=white:fontsize=75:x=10:y=10:"
# command = '{ffmpeg} -i {input} -vf "{text}" -y {output}'.format(ffmpeg=ffmpeg, input=source, text=text_line, output=output)

# Add custom font file
    # NOTE, you need to use /, not \
    # NOTE, your font file path can't have : in it (like C:)
# fontfile = r'//karoo/Pipeline/DCC_Tools/tf_global_tools_new/tf_utilities/utilities/video/bin/fonts/SourceCodePro-Regular.ttf'
# text_line = "drawtext=fontfile={File}: text='Test Text': fontcolor=white: fontsize=75: x=10: y=10:".format(File=fontfile)
# command = '{ffmpeg} -i {input} -vf "{text}" -y {output}'.format(ffmpeg=ffmpeg, input=source, text=text_line, output=output)

# Add text to video for certain seconds
    # This example starts showing the text at 3s and stops at 10s
# text_line = "drawtext=fontfile=/Windows/fonts/calibri.ttf:text='Test Text':fontcolor=white:fontsize=75:x=10:y=10: enable=\'between( t, 3, 10 )\'"
# command = '{ffmpeg} -i {input} -vf "{text}" -y {output}'.format(ffmpeg=ffmpeg, input=source, text=text_line, output=output)

# Add multiple text lines
# text_line_1 = "drawtext=fontfile=/Windows/fonts/calibri.ttf:text='Text1':fontcolor=white:fontsize=75:x=10:y=10: enable=\'between( t, 0, 4 )\'"
# text_line_2 = "drawtext=fontfile=/Windows/fonts/calibri.ttf:text='Text2':fontcolor=white:fontsize=75:x=10:y=30: enable=\'between( t, 2, 10 )\'"
# command = '{ffmpeg} -i {input} -vf "{text_line_1}, {text_line_2}" -y {output}'.format(ffmpeg=ffmpeg, input=source, text_line_1=text_line_1, text_line_2=text_line_2, output=output)

# # Add multiple text lines from an array
# # NOTE: In a case like this, you can use the "ten_frames" just fine, but if you use something like "two_hundred_frames" then youur command becomes too long
# # and the response is "The command line is too long." (which I think is a Windows issue, not ffmpeg issue). To get around this, look at the next solution
# ten_frames = ['hi', 'there', 'my', 'name', 'is', 'hi', 'there', 'my', 'name', 'is']
# fifty_frames = ten_frames + ten_frames + ten_frames + ten_frames + ten_frames
# two_hundred_frames = fifty_frames + fifty_frames + fifty_frames + fifty_frames
# textlines = []
# for index, item in enumerate(ten_frames):
#     # NOTICE HERE: in the next to lines, they are exactly the same except that the one uses "n" and the other "t"
#     # "n" stands for "frame" while "t" stands for "time"
#     text_line = "drawtext=fontfile=/Windows/fonts/calibri.ttf:text='{}':fontcolor=white:fontsize=75:x=10:y=10: enable=\'between( n, {}, {} )\'".format(item, index, index)
#     # text_line = "drawtext=fontfile=/Windows/fonts/calibri.ttf:text='{}':fontcolor=white:fontsize=75:x=10:y=10: enable=\'between( t, {}, {} )\'".format(item, start_time, end_time)
#     textlines.append(text_line)
# command = '{ffmpeg} -i {input} -vf "{textlines}" -y {output}'.format(ffmpeg=ffmpeg, input=source, textlines=', '.join(textlines), output=output)

# # Working with massive command lines (read the above example if you don't understand
# ten_frames = ['hi', 'there', 'my', 'name', 'is', 'hi', 'there', 'my', 'name', 'is']
# fifty_frames = ten_frames + ten_frames + ten_frames + ten_frames + ten_frames
# two_hundred_frames = fifty_frames + fifty_frames + fifty_frames + fifty_frames
# textlines = []
# for index, item in enumerate(two_hundred_frames):
#     text_line = "drawtext=fontfile=/Windows/fonts/calibri.ttf:text='{}':fontcolor=white:fontsize=75:x=10:y=10: enable=\'between( n, {}, {} )\'".format(item, index, index)
#     textlines.append(text_line)
# # First we write the "massive" command to a file
# file = "C:\\Users\\francois.kruger\\Documents\\tf_global\\dev\\tf_ffmpeg\\command.txt"
# f = open(file, "w")
# f.write(',\n'.join(textlines))
# f.close()
# command = '{ffmpeg} -i {input} -filter_complex_script "{file}" -y {output}'.format(ffmpeg=ffmpeg, input=source, file=file, output=output)

# Video from images
# source = 'C:\\Users\\francois.kruger\\Desktop\\awd\\test.%04d.png' # %04d refers to 4 digits, like 0001
# # command = '{ffmpeg} -y -framerate 24 -start_number 0 -i {input} -c:v libx264 -timecode 00:00:04:05 -crf 17 {output}'.format(ffmpeg=ffmpeg, input=source, output=output)
# # -pix_fmt yuv420p is required if you want the video to be playable in windows media player, not sure why though
# command = '{ffmpeg} -framerate 24 -i {input} -pix_fmt yuv420p -y {output}'.format(ffmpeg=ffmpeg, input=source, output=output)

##########################################

subprocess.Popen(command, shell=True)