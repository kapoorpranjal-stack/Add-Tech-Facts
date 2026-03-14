import tkinter as tk
import random
window=tk.Tk()
window.title('Tech Facts')
window.geometry('400x400')
window.config(bg="#d7f5f5")
txt=tk.Label(text='Brightchamps')
txt.pack()
facts=["The first domain name ever registered was 'symbolics.com' on March 15, 1985.",
  "The entire source code of the Apollo 11 guidance computer was less than 64KB, which is smaller than a typical smartphone photo.",
  "IBM's Deep Blue supercomputer became the first computer to defeat a reigning world chess champion, Garry Kasparov, in 1997.",
  "The term 'Wi-Fi' doesn't stand for anything. It's a brand name coined by the Wi-Fi Alliance as a play on 'Hi-Fi'.",
  "The largest hard drive ever built, the Seagate Exos 20TB, can store around 5000 HD movies.",
  "A single Google search requires more computing power than the entire Apollo 11 moon landing mission.",
  "The '404' error code used for broken links on the internet is named after the room 404 at CERN, where the World Wide Web was born.",
  "The iPhone's voice-activated assistant, Siri, was named after a Norwegian woman's name meaning 'beautiful victory'."]
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
        facts_Label.config(text=new_fact)  
        new_facts_entry.delete(0, tk.END)
add_facts_button = tk.Button(window, text="Add Facts", command=add_facts,font=("Arial", 12),bg="#f5f5dc",fg="#000000")
new_facts_entry.pack(pady=10)
add_facts_button.pack(pady=5)
window.mainloop()
