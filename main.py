import tkinter as tk

def submit_school(school_widgets, time_widgets):
  close_widgets(school_widgets)
  
def close_widgets(widgets):
    for i in widgets:
        i.destroy()

def get_school_time(root):
    widgets = []
    time_widgets = [] # <- School Start: Hour, Minute; School End: Hour, Minute; Sleep Wake Up: Hour, Minute; Sleep Fall Asleep: Hour, Minute;
    
    # WIDGETS FOR SCHOOL
    school_label = tk.Label(root, text="Enter schools hours: ")
    school_label.grid(row=0, column=0)
    widgets.append(school_label)
    
    start_label = tk.Label(root, text="Start Time: ")
    start_label.grid(row=1, column=0)
    widgets.append(start_label)
    
    start_hour_inp = tk.Spinbox(root, from_=1, to=12, wrap=True, width=2)
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
    
    end_hour_inp = tk.Spinbox(root, from_=1, to=12, wrap=True, width=2)
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
    
    wake_up_hour_inp = tk.Spinbox(root, from_=1, to=12, wrap=True, width=2)
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
    
    to_bed_hour_inp = tk.Spinbox(root, from_=1, to=12, wrap=True, width=2)
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
root.geometry("520x420")
root.resizable(False, False)

school_widgets = get_school_time(root)

root.mainloop()