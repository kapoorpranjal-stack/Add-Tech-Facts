import tkinter as tk
import random
window=tk.Tk()
window.title('Tech Facts')
window.geometry('400x400')
window.config(bg="#d7f5f5")
txt=tk.Label(text='Brightchamps')
txt.pack()
facts=["The sun is a star","The earth is round","The moon is not a planet",
       "The sun is not a planet","The earth is not a planet",
       "The moon is not a star","The sun is not a moon",
      ]
facts_Label = tk.Label(window, text="",wraplength=300,font=("Arial", 12))
def show_facts():
  fact=random.choice(facts)
  facts_Label.config(text=fact)
   # Create a button widget   
facts_button = tk.Button(window, text="Show Facts", command=show_facts)
facts_Label.pack(pady=20)
facts_button.pack(pady=10)
new_facts_entry = tk.Entry(window, width=30,font=("Arial", 12))
def add_facts():
    new_fact = new_facts_entry.get().strip()
    if new_fact:
        facts.append(new_fact)
        new_facts_entry.delete(0, tk.END)
add_facts_button = tk.Button(window, text="Add Facts", command=add_facts,font=("Arial", 12),bg="#f5f5dc",fg="#000000")
new_facts_entry.pack(pady=10)
add_facts_button.pack(pady=5)
window.mainloop()
