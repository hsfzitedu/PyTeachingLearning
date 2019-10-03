# https://docs.python.org/3/library/tkinter.ttk.html
# https://www.python-course.eu/tkinter_labels.php
# http://www.runoob.com/python/att-time-time.html


import tkinter as tk
import time

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    # label.config(text=str(counter))
    label.config(text=time.asctime( time.localtime(time.time())))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()

root.mainloop()
