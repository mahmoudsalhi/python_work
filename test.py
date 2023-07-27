import tkinter as tk
from tkinter import messagebox

count = 0
mark = 'X'
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def win(current_mark):
    if (button1["text"] == button2["text"] == button3["text"] == current_mark or
        button4["text"] == button5["text"] == button6["text"] == current_mark or
        button7["text"] == button8["text"] == button9["text"] == current_mark or
        button1["text"] == button4["text"] == button7["text"] == current_mark or
        button2["text"] == button5["text"] == button8["text"] == current_mark or
        button3["text"] == button6["text"] == button9["text"] == current_mark or
        button1["text"] == button5["text"] == button9["text"] == current_mark or
        button3["text"] == button5["text"] == button7["text"] == current_mark):
        return True
    return False


def checker(digit):
    global count, mark,digits

    if digit in digits:
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'

        if digit == 1:
            button1.config(text=mark)
        elif digit == 2:
            button2.config(text=mark)
        elif digit == 3:
            button3.config(text=mark)
        elif digit == 4:
            button4.config(text=mark)
        elif digit == 5:
            button5.config(text=mark)
        elif digit == 6:
            button6.config(text=mark)
        elif digit == 7:
            button7.config(text=mark)
        elif digit == 8:
            button8.config(text=mark)
        elif digit == 9:
            button9.config(text=mark)

        count += 1

        if count >= 5: 
            if win(mark):
                message = f"Player1 wins" if mark == 'X' else "Player2 wins"
                messagebox.showinfo("Game Over", message)
                window.destroy()
                return

        if count > 8:
            messagebox.showinfo("Game Over", "Match Tied")
            window.destroy()
            return

        digits.remove(digit)


window = tk.Tk()
window.title("Tic-Tac-Toe")

button_size = 6  
button_font = ('Helvetica', 24, 'bold') 

button1 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(1))
button2 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(2))
button3 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(3))
button4 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(4))
button5 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(5))
button6 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(6))
button7 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(7))
button8 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(8))
button9 = tk.Button(window, text="", font=button_font, width=button_size, height=button_size, command=lambda: checker(9))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)


window.mainloop()