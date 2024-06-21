import tkinter as tk
from tkinter import messagebox

def choice():
    name1 = entry_name1.get()
    name2 = entry_name2.get()
    choice1 = entry_choice1.get().lower()
    choice2 = entry_choice2.get().lower()

    if choice1==choice2:
        result = "It's a Tie."
    elif(choice1=="s" and choice2=="w") or (choice1=="w" and choice2=="g") or (choice1=="g" or choice2=="s"):
        result = f"{name1} wins!"

    elif(choice2=="s" and choice1=="w") or (choice2=="w" and choice1=="g") or (choice2=="g" and choice1=="s"):
        result =f"{name2} wins!"
    else:
        result = "Invalid choice!"
    result_label.config(text=result)
def quit_app():
    root.destroy()

root = tk.Tk()
root.title("SNAKE,WATER,GUN GAME.")

tk.Label(root,text="Enter the 1st user name:").pack()
entry_name1 = tk.Entry(root)
entry_name1.pack(pady=5)

tk.Label(root,text="Enter the 2nd user name:").pack()
entry_name2 = tk.Entry(root)
entry_name2.pack(pady=6)

tk.Label(root,text="Enter the 1st person choice: (S,W,G)").pack()
entry_choice1 = tk.Entry(root)
entry_choice1.pack(pady=6)

tk.Label(root,text="Enter the 2nd user choice: (S,W,G)").pack()
entry_choice2 = tk.Entry(root)
entry_choice2.pack(pady=6)

roll_button = tk.Button(root,text="CLICK HERE TO SEE THE RESULT",command=choice)
roll_button.pack(pady=20)

quit_button = tk.Button(root,text="Quit",command=quit_app)
quit_button.pack(pady=20)

result_label = tk.Label(root,text="")
result_label.pack(pady=60)







root.mainloop()