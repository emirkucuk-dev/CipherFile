import tkinter as tk
from tkinter import messagebox, filedialog

from caesar import en_caesar, de_caesar
from xor import en_XOR, de_XOR
from des3 import en_3des, de_3des
import aes
from file import read_text_file, write_text_file


class App:
    def __init__(self, root):
        self.input_path = None
        self.output_path = None
        self.root = root
        self.root.title("Şifreleme Uygulaması")
        self.root.geometry("700x400")
        self.root.configure(bg="#d9d9d9")

        # ANA FRAME
        main_frame = tk.Frame(root, bg="#d9d9d9")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        card = tk.Frame(main_frame, bg="#d9d9d9", bd=1, relief="ridge")
        card.pack(expand=True, fill="both", padx=10, pady=10)
        self.card = card

        title_label = tk.Label(
            card,
            text="Şifreleme Uygulamasına Hoşgeldiniz:)",
            font=("Arial", 18, "bold"),
            bg="#d9d9d9",
            fg="#284b63",
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))

        # DOSYA FRAME
        file_frame = tk.Frame(self.card, bg="#d9d9d9")
        file_frame.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=5)

        header_file = tk.Label(
            file_frame,
            text="Dosya Seçimi",
            font=("Arial", 11, "bold"),
            bg="#d9d9d9",
            fg="#284b63",
        )
        header_file.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 5))

        # Giriş dosyası
        tk.Label(file_frame, text="Giriş dosyası:", bg="#d9d9d9", fg="#284b63") \
            .grid(row=1, column=0, sticky="e", padx=5, pady=3)

        tk.Button(file_frame, text="Seç", command=self.select_input) \
            .grid(row=1, column=1, sticky="w", padx=5, pady=3)

        self.input_label = tk.Label(
            file_frame,
            text="Seçili dosya yok",
            bg="#d9d9d9",
            fg="#284b63",
            anchor="w",
        )
        self.input_label.grid(row=1, column=3, sticky="w", padx=5, pady=3)

        # Çıkış dosyası
        tk.Label(file_frame, text="Çıkış dosyası:", bg="#d9d9d9", fg="#284b63") \
            .grid(row=2, column=0, sticky="e", padx=5, pady=3)

        tk.Button(file_frame, text="Seç", command=self.select_output) \
            .grid(row=2, column=1, sticky="w", padx=5, pady=3)

        self.output_label = tk.Label(
            file_frame,
            text="Kaydedilecek dosya yok",
            bg="#d9d9d9",
            fg="#284b63",
            anchor="w",
        )
        self.output_label.grid(row=2, column=3, sticky="w", padx=5, pady=3)

        # CONFIG FRAME
        config_frame = tk.Frame(self.card, bg="#d9d9d9")
        config_frame.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=(10, 5))

        header_config = tk.Label(
            config_frame,
            text="Ayarlamalar",
            font=("Arial", 11, "bold"),
            bg="#d9d9d9",
            fg="#284b63",
        )
        header_config.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 5))

        # Algoritma seçimi
        tk.Label(config_frame, text="Algoritma:", bg="#d9d9d9", fg="#000") \
            .grid(row=1, column=0, sticky="e", padx=5, pady=3)

        self.alg_var = tk.StringVar(value="Caesar")

        algo_frame = tk.Frame(config_frame, bg="#d9d9d9")
        algo_frame.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=3)

        tk.Radiobutton(
            algo_frame, text="Caesar",
            variable=self.alg_var, value="Caesar",
            bg="#d9d9d9", fg="#000", selectcolor="#d9d9d9",
        ).pack(side="left", padx=5)

        tk.Radiobutton(
            algo_frame, text="XOR",
            variable=self.alg_var, value="XOR",
            bg="#d9d9d9", fg="#000", selectcolor="#d9d9d9",
        ).pack(side="left", padx=5)

        tk.Radiobutton(
            algo_frame, text="3DES",
            variable=self.alg_var, value="3DES",
            bg="#d9d9d9", fg="#000", selectcolor="#d9d9d9",
        ).pack(side="left", padx=5)

        tk.Radiobutton(
            algo_frame, text="AES",
            variable=self.alg_var, value="AES",
            bg="#d9d9d9", fg="#000", selectcolor="#d9d9d9",
        ).pack(side="left", padx=5)

        # Anahtar
        tk.Label(config_frame, text="Anahtar / Shift:", bg="#d9d9d9", fg="#000") \
            .grid(row=2, column=0, sticky="e", padx=5, pady=3)

        self.key_entry = tk.Entry(config_frame, width=35)
        self.key_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=3)

        # BUTONLAR
        button_frame = tk.Frame(self.card, bg="#d9d9d9")
        button_frame.grid(row=3, column=0, columnspan=3, pady=(20, 10))

        tk.Button(
            button_frame,
            text="Şifrele",
            relief="flat",
            height=1,
            width=15,
            command=self.encrypt,
            bg="#284b63",
            fg="#ffffff",
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Çöz",
            relief="flat",
            height=1,
            width=15,
            command=self.decrypt,
            bg="#284b63",
            fg="#ffffff",
        ).pack(side="left", padx=10)

    # ------------------ DOSYA SEÇİMİ ------------------

    def select_input(self):
        path = filedialog.askopenfilename()
        if path:
            self.input_path = path
            self.input_label.config(text=path)

    def select_output(self):
        path = filedialog.asksaveasfilename(
            title="Çıkış dosyasını seç",
            defaultextension=".enc",
            filetypes=[
                ("Şifreli dosya", "*.enc"),
                ("Tüm dosyalar", "*.*"),
            ],
        )
        if path:
            self.output_path = path
            self.output_label.config(text=path)

    # ------------------ ORTAK KONTROLLER ------------------

    def check_common(self):
        if not self.input_path:
            messagebox.showerror("Hata", "Lütfen giriş dosyasını seçiniz.")
            return False

        if not self.output_path:
            messagebox.showerror("Hata", "Lütfen çıkış dosyasını seçiniz.")
            return False

        key = self.key_entry.get().strip()
        if key == "":
            messagebox.showerror("Hata", "Anahtar / shift boş bırakılamaz!")
            return False

        algo = self.alg_var.get()

        if algo == "Caesar":
            try:
                int(key)
            except ValueError:
                messagebox.showerror("Hata", "Caesar için shift değeri bir sayı olmalıdır.")
                return False

        if algo == "AES" and len(key) < 16:
            messagebox.showerror("Hata", "AES için anahtar en az 16 karakter olmalıdır.")
            return False

        if algo == "3DES" and len(key) < 3:
            messagebox.showerror("Hata", "3DES için anahtar en az 3 karakter olmalıdır.")
            return False

        return True

    # ------------------ ŞİFRELEME ------------------

    def encrypt(self):
        if not self.check_common():
            return

        data = read_text_file(self.input_path)
        algo = self.alg_var.get()
        key_str = self.key_entry.get().strip()

        try:
            if algo == "Caesar":
                shift = int(key_str)
                result = en_caesar(data, shift)

            elif algo == "XOR":
                result = en_XOR(data, key_str)

            elif algo == "3DES":
                result = en_3des(data, key_str)

            elif algo == "AES":
                result = aes.en_aes(data, key_str)

            else:
                messagebox.showerror("Hata", "Algoritma seçilmedi.")
                return

        except Exception as e:
            messagebox.showerror("Hata", f"Şifreleme sırasında hata oluştu:\n{e}")
            return

        write_text_file(self.output_path, result)
        messagebox.showinfo("Başarılı", "Şifreleme işleminiz tamamlandı.")

    # ------------------ ÇÖZME ------------------

    def decrypt(self):
        if not self.check_common():
            return

        data = read_text_file(self.input_path)
        algo = self.alg_var.get()
        key_str = self.key_entry.get().strip()

        try:
            if algo == "Caesar":
                shift = int(key_str)
                result = de_caesar(data, shift)

            elif algo == "XOR":
                result = de_XOR(data, key_str)

            elif algo == "3DES":
                result = de_3des(data, key_str)

            elif algo == "AES":
                result = aes.de_aes(data, key_str)

            else:
                messagebox.showerror("Hata", "Algoritma seçilmedi.")
                return

        except Exception as e:
            messagebox.showerror("Hata", f"Çözme sırasında hata oluştu:\n{e}")
            return

        write_text_file(self.output_path, result)
        messagebox.showinfo("Başarılı", "Çözme işleminiz tamamlandı.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

