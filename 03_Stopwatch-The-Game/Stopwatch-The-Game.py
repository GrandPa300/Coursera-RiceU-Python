# template for "Stopwatch: The Game"

import simplegui

# define global variables

time_count = 0
tot_stop = 0
suc_stop = 0

# timer in 0.1 sec interval
interval = 100

# Add a global variable "running" to 
# detect the status of stop watch. i.e. run/stop
running = False

# define helper function format that converts interger
# counting tenths of seconds into formatted string A:BC.D

    # Fill-up empty digits if value < 10
    # If valus is 0, make it as "00"
def single_convert(num):
    if num == 0:
        str_num = "00"
    elif num < 10:
        str_num = "0"+str(num)
    else:
        str_num = str(num)
    return str_num

    # Convert into string
def convert(time_count):
    hou = int(time_count / 36000)
    min = int((time_count - hou * 36000)/600)
    sec = int((time_count - hou * 36000 - min *600)/10)
    tenth_sec = time_count % 10
    
    time_string = single_convert(hou) + ':' \
                + single_convert(min) + ':' \
                + single_convert(sec) + '.' \
                + str(tenth_sec)[0:1]
    return time_string

# deinfe event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global running
    running = True
    timer.start()

    # Added an additional function into stop() 
    # Count the success-stop/total-stop based on status of stop watch
    # If the stopwatch has alreayd stopped, hitting "Stop" won't do anything
    
def stop():
    global suc_stop, tot_stop, running
    if running == False:
        pass
    elif convert(time_count)[-1]=="0":
        tot_stop += 1
        suc_stop += 1
    else:
        tot_stop += 1
    running = False
    timer.stop()
    return tot_stop, suc_stop
    
def reset():
    global time_count, suc_stop, tot_stop, running
    time_count = 0
    suc_stop = 0
    tot_stop = 0
    running = False
    timer.stop()

# define event handler for timer with 0.1 sec interval

def time_handler():
    global time_count
    time_count += 1
    
def draw_handler(canvas):
    time_string = convert(time_count)
    canvas.draw_text(time_string, (45, 110), 30, 'Lime')
    canvas.draw_text(str(suc_stop) + '/' + str(tot_stop), (160,20),15,"White",)

# create frame

frame = simplegui.create_frame("Stopwatch: The Game",200,200)
frame.set_draw_handler(draw_handler)

# register event handlers

button_start = frame.add_button('Start', start, 100)
botton_stop = frame.add_button('Stop', stop, 100)
botton_reset = frame.add_button('Reset', reset, 100)
timer = simplegui.create_timer(interval, time_handler)

# start timer and frame

frame.start()
reset()

# remember to review the grading rubric