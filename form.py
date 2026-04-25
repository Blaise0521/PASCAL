import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Main Application Setup ---
class Assignment:
    def submit_form():
        """Handles the form submission and data extraction."""
        title = title_entry.get()
        due_date = date_entry.get()
        time_taken = time_entry.get()

        # Basic validation to ensure fields aren't empty
        if not title or not due_date or not time_taken:
            messagebox.showwarning("Input Error", "Please fill out all fields before submitting.")
            return

        # Display the collected data in a popup window
        summary = f"Task Saved Successfully!\n\nTitle: {title}\nDue Date: {due_date}\nTime to Complete: {time_taken}"
        messagebox.showinfo("Submission Success", summary)

        # Clear the form fields after successful submission
        title_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

    def __init__(self):
        root = tk.Tk()
        root.title("Task Entry Form")
        root.geometry("400x250")
        root.resizable(False, False) # Prevents the window from being resized
        
        # Main frame for clean padding around the edges
        frame = ttk.Frame(root, padding="20 20 20 20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # --- Field 1: Task Title ---
        ttk.Label(frame, text="Task Title:").grid(row=0, column=0, sticky=tk.W, pady=10, padx=5)
        title_entry = ttk.Entry(frame, width=20)
        title_entry.grid(row=0, column=1, sticky=tk.EW, pady=10, padx=5)
        
        self.title = title_entry.get()
        
        # --- Field 2: Due Date ---
        ttk.Label(frame, text="Due Date (MM-DD-YYYY):").grid(row=1, column=0, sticky=tk.W, pady=10, padx=5)
        date_entry = ttk.Entry(frame, width=20)
        date_entry.grid(row=1, column=1, sticky=tk.EW, pady=10, padx=5)
        
        self.date = date_entry.get()
        
        ttk.Label(frame, text="Time Due: (HH:MM:SS)").grid(row=2, column=0, sticky=tk.W, pady=10, padx=5)
        time_due_entry = ttk.Entry(frame, width=20)
        time_due_entry.grid(row=2, column=1, sticky=tk.EW, pady=10, padx=5)
        
        # --- Field 3: Time Taken ---
        ttk.Label(frame, text="Time to Complete (e.g., 2 hrs):").grid(row=3, column=0, sticky=tk.W, pady=10, padx=5)
        time_entry = ttk.Entry(frame, width=20)
        time_entry.grid(row=3, column=1, sticky=tk.EW, pady=10, padx=5)
        
        self.time=time_entry.get()
        
        # --- Submit Button ---
        submit_btn = ttk.Button(frame, text="Submit", command=submit_form)
        submit_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        root.mainloop()