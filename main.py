import tkinter as tk
from form import Assignment

def submit_school(school_widgets, time_widgets):
    times = [i.get() for i in time_widgets]
    
    close_widgets(school_widgets)
    schedule(times)
    
    
  
  
def close_widgets(widgets):
    for i in widgets:
        i.destroy()

def new_assignment():
    ass = Assignment()
    
    print(ass.date)
    print(ass.time)
    print(ass.title)

def schedule(times):
    
    canvas = tk.Canvas(root, width=900, height=600, bg="#260F26")
    canvas.pack()
    screen_width = root.winfo_width()
    columns = (int(times[6])-int(times[4])+1)
    col_offset = screen_width // columns
    
    
    button = tk.Button(root, text="Add Assignment", command=new_assignment)
    button.place(x=screen_width/2, y=0)
    
    
    for i in range(int(times[4]), int(times[6])+1):
        time_label = tk.Label(root, text=f"{i}", bg="#260F26")
        time_label.place(x=(i-int(times[4]))*col_offset, y=50)
        
        
    top_left_x = (int(times[0])-int(times[4]))*col_offset
    bottom_right_x = (int(times[2])-int(times[4]))*col_offset
    school = canvas.create_rectangle(top_left_x, 100, bottom_right_x, 150, fill="#404E7C")
    
    school_label = tk.Label(root, text="In School", bg="#404E7C")
    school_label.place(x=top_left_x, y=100)
    

def get_school_time():
    widgets = []
    time_widgets = [] # <- School Start(0, 1): Hour, Minute; School End(2,3): Hour, Minute; Sleep Wake Up(4,5): Hour, Minute; Sleep Fall Asleep(6,7): Hour, Minute;
    
    # WIDGETS FOR SCHOOL
    school_label = tk.Label(root, text="Enter schools hours: ")
    school_label.grid(row=0, column=0)
    widgets.append(school_label)
    
    start_label = tk.Label(root, text="Start Time: ")
    start_label.grid(row=1, column=0)
    widgets.append(start_label)
    
    start_hour_inp = tk.Spinbox(root, from_=1, to=24, wrap=True, width=2)
    start_hour_inp.grid(row=1, column=1)
    widgets.append(start_hour_inp)
    time_widgets.append(start_hour_inp)
    
    start_colon_label = tk.Label(root, text=":")
    start_colon_label.grid(row=1, column=2)
    widgets.append(start_colon_label)
    
    start_minute_inp = tk.Spinbox(root, from_=00, to=59, wrap=True,width=2)
    start_minute_inp.grid(row=1, column=3)
    widgets.append(start_minute_inp)
    time_widgets.append(start_minute_inp)
    
    end_label = tk.Label(root, text="End Time: ")
    end_label.grid(row=2, column=0)
    widgets.append(end_label)
    
    end_hour_inp = tk.Spinbox(root, from_=1, to=24, wrap=True, width=2)
    end_hour_inp.grid(row=2, column=1)
    widgets.append(end_hour_inp)
    time_widgets.append(end_hour_inp)
    
    end_colon_label = tk.Label(root, text=":")
    end_colon_label.grid(row=2, column=2)
    widgets.append(end_colon_label)
    
    end_minute_inp = tk.Spinbox(root, from_=00, to=59, wrap=True,width=2)
    end_minute_inp.grid(row=2, column=3)
    widgets.append(end_minute_inp)
    time_widgets.append(end_minute_inp)
    
    
    
    # WIDGETS FOR SLEEP
    sleep_label = tk.Label(root, text="Enter sleeping hours: ")
    sleep_label.grid(row=3, column=0)
    widgets.append(sleep_label)
    
    wake_up_label = tk.Label(root, text="Wake up time:")
    wake_up_label.grid(row=4, column=0)
    widgets.append(wake_up_label)
    
    wake_up_hour_inp = tk.Spinbox(root, from_=1, to=24, wrap=True, width=2)
    wake_up_hour_inp.grid(row=4, column=1)
    widgets.append(wake_up_hour_inp)
    time_widgets.append(wake_up_hour_inp)
    
    wake_up_colon_label = tk.Label(root, text=":")
    wake_up_colon_label.grid(row=4, column=2)
    widgets.append(wake_up_colon_label)
    
    wake_up_minute_inp = tk.Spinbox(root, from_=00, to=59, wrap=True,width=2)
    wake_up_minute_inp.grid(row=4, column=3)
    widgets.append(wake_up_minute_inp)
    time_widgets.append(wake_up_minute_inp)
    
    
    to_bed_label = tk.Label(root, text="Go to bed time:")
    to_bed_label.grid(row=5, column=0)
    widgets.append(to_bed_label)
    
    to_bed_hour_inp = tk.Spinbox(root, from_=1, to=24, wrap=True, width=2)
    to_bed_hour_inp.grid(row=5, column=1)
    widgets.append(to_bed_hour_inp)
    time_widgets.append(to_bed_hour_inp)
    
    to_bed_colon_label = tk.Label(root, text=":")
    to_bed_colon_label.grid(row=5, column=2)
    widgets.append(to_bed_colon_label)
    
    to_bed_colon_label = tk.Spinbox(root, from_=00, to=59, wrap=True,width=2)
    to_bed_colon_label.grid(row=5, column=3)
    widgets.append(to_bed_colon_label)
    time_widgets.append(to_bed_colon_label)
    
    
    submit_button = tk.Button(root, text="Submit", command= lambda: submit_school(widgets, time_widgets))
    submit_button.grid(row=10, column=0)
    widgets.append(submit_button)
    
    
    return widgets

root = tk.Tk()
root.title("Assignment Tracker")
root.geometry("900x600")
root.configure(bg='#260F26') 
root.resizable(False, False)

school_widgets = get_school_time()

root.mainloop()