import tkinter as tk
from tkinter import messagebox
import random

class BinarySearch:
    def __init__(self):
        self.lower_bound = 1
        self.upper_bound = 100
        self.current_guess = random.randint(self.lower_bound, self.upper_bound)
        self.current_guess_attempts = 0

    def guess(self, value):
        self.current_guess_attempts += 1
        if value == self.current_guess:
            return "correct"
        elif value < self.current_guess:
            self.lower_bound = value + 1
            return "too low"
        else:
            self.upper_bound = value - 1
            return "too high"

    def next_guess(self):
        if self.lower_bound <= self.upper_bound:
            self.current_guess = (self.lower_bound + self.upper_bound) // 2
        return self.current_guess

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Mystery Numeral Quest')
        self.geometry('300x300')
        self.initUI()

    def initUI(self):
        # Mendapatkan ukuran jendela
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()

        # Mengatur posisi tengah jendela
        x_coordinate = (self.winfo_screenwidth() // 2) - (window_width // 2)
        y_coordinate = (self.winfo_screenheight() // 2) - (window_height // 2)
        self.geometry(f'+{x_coordinate}+{y_coordinate}')

        self.instructions = tk.Label(self, text='Mystery Numeral Quest', font=('Times New Roman', 18))
        self.instructions.place(relx=0.5, rely=0.15, anchor='center')

        # Tombol Menu Main
        self.main_menu_button = tk.Button(self, text='Main', command=self.start_game, font=('Arial', 14))
        self.main_menu_button.place(relx=0.5, rely=0.4, anchor='center')

        # Tombol Keluar
        self.exit_button = tk.Button(self, text='Keluar', command=self.quit, font=('Arial', 14))
        self.exit_button.place(relx=0.5, rely=0.55, anchor='center')

    def start_game(self):
        self.destroy()  # Tutup menu utama
        app = GuessingGame()  # Mulai permainan tebak angka
        app.mainloop()

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Mystery Numeral Quest')
        self.geometry('300x300')
        self.binary_search = BinarySearch()
        self.initUI()

    def initUI(self):
        # Mendapatkan ukuran jendela
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()

        # Mengatur posisi tengah jendela
        x_coordinate = (self.winfo_screenwidth() // 2) - (window_width // 2)
        y_coordinate = (self.winfo_screenheight() // 2) - (window_height // 2)
        self.geometry(f'+{x_coordinate}+{y_coordinate}')

        # Label Tebak angka antara 1 dan 100
        self.instructions = tk.Label(self, text='Tebak angka antara 1 sampai 100:', font=('Times New Roman', 14))
        self.instructions.place(relx=0.5, rely=0.2, anchor='center')

        # Field input tebakan
        self.guess_input = tk.Entry(self, font=('Arial', 18), justify="center")
        self.guess_input.insert(0, '')
        self.guess_input.place(relx=0.5, rely=0.3, anchor='center')

        # Tombol Tebak
        self.guess_button = tk.Button(self, text='Tebak', command=self.check_guess, font=('Arial', 14))
        self.guess_button.place(relx=0.5, rely=0.45, anchor='center')

        # Label hasil
        self.result_label = tk.Label(self, text='', font=('Times New Roman', 14))
        self.result_label.place(relx=0.5, rely=0.6, anchor='center')

        # Tombol Coba Lagi
        self.retry_button = tk.Button(self, text='Coba Lagi', command=self.reset_game, font=('Arial', 14))
        self.retry_button.config(state=tk.DISABLED)
        self.retry_button.place(relx=0.5, rely=0.75, anchor='center')

        # Tombol Kembali
        self.back_button = tk.Button(self, text='Kembali', command=self.return_to_main_menu, font=('Arial', 14))
        self.back_button.place(relx=0.5, rely=0.9, anchor='center')

    def check_guess(self):
        guess_text = self.guess_input.get()
        self.result_label.config(text='')
        try:
            guess = int(guess_text)
            if guess < 1 or guess > 100:
                self.result_label.config(text='Tebakan harus antara 1 dan 100!')
                return
        except ValueError:
            self.result_label.config(text='Harap masukkan angka yang valid.')
            return

        result = self.binary_search.guess(guess)

        if result == "correct":
            points = 100 - self.binary_search.current_guess_attempts
            if self.binary_search.current_guess_attempts == 1:
                messagebox.showinfo('Info', f'SELAMAT!!!\nAnda berhasil menebak angkanya.\n' f'Poin Anda: {points}')
            else:
                messagebox.showinfo('Info', f'SELAMAT!!!\nAnda berhasil menebak angkanya dalam {self.binary_search.current_guess_attempts} kali percobaan.\n' f'Poin Anda: {points}')
            self.guess_button.config(state=tk.DISABLED)
            self.retry_button.config(state=tk.NORMAL)
        elif result == "too low":
            messagebox.showinfo('Info', 'Tebakan Anda terlalu rendah.\nCoba lagi!')
        else:
            messagebox.showinfo('Info', 'Tebakan Anda terlalu tinggi.\nCoba lagi!')

    def reset_game(self):
        self.binary_search = BinarySearch()
        self.result_label.config(text='')
        self.guess_button.config(state=tk.NORMAL)
        self.retry_button.config(state=tk.DISABLED)
        self.guess_input.delete(0, tk.END)

    def return_to_main_menu(self):
        self.destroy()  # Tutup permainan
        menu = MainMenu()  # Kembali ke menu utama
        menu.mainloop()

if __name__ == '__main__':
    menu = MainMenu()
    menu.mainloop()
