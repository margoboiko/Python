from tkinter import *


class Block:
    def __init__(self, master):
        self.lab1 = Label(master, width=20, text=' Перше число:', pady=10)
        self.ent1 = Entry(master, width=20)

        self.lab2 = Label(master, width=20, text='Друге число:', pady=10)
        self.ent2 = Entry(master, width=20)

        self.but1 = Button(master,
                          text="НСД", pady=10)
        self.but2 = Button(master,
                          text="НСК", pady=10)

        self.num = Label(master, width=40, pady=20, text='Результат:')

        self.but1['command'] = self.count1
        self.lab1.pack()
        self.ent1.pack()
        self.lab2.pack()
        self.ent2.pack()
        self.but1.pack()

        self.but2['command'] = self.count2
        self.lab1.pack()
        self.ent1.pack()
        self.lab2.pack()
        self.ent2.pack()
        self.but2.pack()
        self.num.pack()

    def count1(self):
        val1 = self.ent1.get()
        val2 = self.ent2.get()

        num1 = int(val1)
        num2 = int(val2)

        while num1 != 0 and num2 != 0:
            if num1 > num2:
                    num1 %= num2
            else:
                    num2 %= num1

        self.num['text'] = 'Результат: ' + str(num1 + num2)

    def count2(self):
        val1 = self.ent1.get()
        val2 = self.ent2.get()

        num1 = int(val1)
        num2 = int(val2)

        nsd = num1 * num2

        while num1 != 0 and num2 != 0:
            if num1 > num2:
                    num1 %= num2
            else:
                    num2 %= num1

        self.num['text'] = 'Результат: ' + str((nsd)//(num1 + num2))


root = Tk()
root.title('Варіант 2')

main = Block(root)

root.mainloop()