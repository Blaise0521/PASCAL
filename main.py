import tkinter as tk

root = tk.Tk()
root.title("Assignment Tracker")
root.geometry("520x420")
root.resizable(False, False)

assignment_types = ["Homework", "Project", "Presentation"]
color_map = {
    "Homework": "#a8d5e2",
    "Project": "#ffd28e",
    "Presentation": "#c2f0c2",
}

form_frame = tk.Frame(root, padx=12, pady=12)
form_frame.grid(row=0, column=0, sticky="nw")

type_label = tk.Label(form_frame, text="Assignment Type:")
type_label.grid(row=0, column=0, sticky="w", pady=(0, 6))
assignment_type_var = tk.StringVar(value=assignment_types[0])
type_menu = tk.OptionMenu(form_frame, assignment_type_var, *assignment_types)
type_menu.grid(row=0, column=1, sticky="ew", pady=(0, 6))

name_label = tk.Label(form_frame, text="Assignment Name:")
name_label.grid(row=1, column=0, sticky="w", pady=(0, 6))
name_entry = tk.Entry(form_frame, width=28)
name_entry.grid(row=1, column=1, sticky="ew", pady=(0, 6))

estimate_label = tk.Label(form_frame, text="Estimated Time (hours):")
estimate_label.grid(row=2, column=0, sticky="w", pady=(0, 10))
estimate_entry = tk.Entry(form_frame, width=28)
estimate_entry.grid(row=2, column=1, sticky="ew", pady=(0, 10))

message_label = tk.Label(form_frame, text="", fg="red")
message_label.grid(row=3, column=0, columnspan=2, sticky="w")

assignments_frame = tk.Frame(root, padx=12, pady=12)
assignments_frame.grid(row=1, column=0, sticky="nsew")

assignments_title = tk.Label(assignments_frame, text="Assignments", font=(None, 12, "bold"))
assignments_title.pack(anchor="w")

boxes_frame = tk.Frame(assignments_frame)
boxes_frame.pack(fill="both", expand=True)

boxes_canvas = tk.Canvas(boxes_frame, borderwidth=0, highlightthickness=0, width=480, height=260)
scrollbar = tk.Scrollbar(boxes_frame, orient="vertical", command=boxes_canvas.yview)
scrollable_frame = tk.Frame(boxes_canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda event: boxes_canvas.configure(scrollregion=boxes_canvas.bbox("all"))
)

boxes_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
boxes_canvas.configure(yscrollcommand=scrollbar.set)

boxes_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

assignment_count = 0

def add_assignment():
    global assignment_count
    assignment_type = assignment_type_var.get().strip()
    assignment_name = name_entry.get().strip()
    estimate_text = estimate_entry.get().strip()

    if not assignment_name:
        message_label.config(text="Please enter the assignment name.")
        return

    if not estimate_text:
        message_label.config(text="Please enter estimated time.")
        return

    try:
        estimate = float(estimate_text)
        if estimate <= 0:
            raise ValueError
    except ValueError:
        message_label.config(text="Estimated time must be a positive number.")
        return

    message_label.config(text="")
    bg_color = color_map.get(assignment_type, "#e0e0e0")
    assignment_count += 1

    box = tk.Frame(scrollable_frame, bg=bg_color, bd=2, relief="raised", padx=8, pady=8)
    box.pack(fill="x", pady=5)

    title = tk.Label(box, text=f"{assignment_type}: {assignment_name}", bg=bg_color, font=(None, 10, "bold"))
    title.pack(anchor="w")

    details = tk.Label(box, text=f"Estimated time: {estimate} hour(s)", bg=bg_color)
    details.pack(anchor="w", pady=(4, 0))

    status = tk.Label(box, text=f"Task #{assignment_count}", bg=bg_color, fg="#555555")
    status.pack(anchor="e")

    name_entry.delete(0, tk.END)
    estimate_entry.delete(0, tk.END)

    scrollable_frame.update_idletasks()
    boxes_canvas.yview_moveto(1.0)

add_button = tk.Button(form_frame, text="Add Assignment", command=add_assignment, bg="#4a86e8", fg="white")
add_button.grid(row=4, column=0, columnspan=2, pady=(6, 0), sticky="ew")

root.mainloop()
