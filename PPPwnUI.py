import tkinter as tk
from tkinter import messagebox, filedialog
import psutil
import subprocess
import os
import sys

# Tabs
PPPWN   = "PPPwn"
GOLDHEN = "GOLDHEN"
PS4HEN  = "PS4HEN"
LINUX   = "Linux"
CUSTOM  = "Custom"

# GOLDHEN Options
GOLDHEN_900 = "Goldhen for 9.00"
GOLDHEN_950 = "Goldhen for 9.50"
GOLDHEN_951 = "Goldhen for 9.51"
GOLDHEN_960 = "Goldhen for 9.60"
GOLDHEN_1000 = "Goldhen for 10.00"
GOLDHEN_1001 = "Goldhen for 10.01"
GOLDHEN_1050 = "Goldhen for 10.50"
GOLDHEN_1070 = "Goldhen for 10.70"
GOLDHEN_1071 = "Goldhen for 10.71"
GOLDHEN_1100 = "Goldhen for 11.00"

# PS4HEN Options
VTX_800  = "VTX HEN for 8.00"
VTX_803  = "VTX HEN for 8.03"
VTX_850  = "VTX HEN for 8.50"
VTX_852  = "VTX HEN for 8.52"
VTX_903  = "VTX HEN for 9.03"
VTX_904  = "VTX HEN for 9.04"
VTX_1000 = "VTX HEN for 10.00"
VTX_1001 = "VTX HEN for 10.01"
VTX_1050 = "VTX HEN for 10.50"
VTX_1070 = "VTX HEN for 10.70"
VTX_1071 = "VTX HEN for 10.71"
VTX_1100 = "VTX HEN for 11.00"

# Linux Options
LINUX_1GB = "Linux 1GB 11.00"
LINUX_2GB = "Linux 2GB 11.00"
LINUX_3GB = "Linux 3GB 11.00"
LINUX_4GB = "Linux 4GB 11.00"

def get_network_interface_names():
    interfaces = psutil.net_if_addrs()
    return interfaces.keys()

class App:
    def __init__(self, master):
        self.master = master
        master.title("PPPwnUI v3.07 by Memz (mod by aldostools)")

        # taille de la fenêtre
        master.geometry("420x380")
        #master.eval('tk::PlaceWindow . center')

        # Set the resizable property False
        master.resizable(False, False)

        # logo d'application
        if sys.platform == "linux":
            pass
        else :
            master.iconbitmap("media/logo.ico")

        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        master.bind('<Return>', self.button_click)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=master.quit)

        self.exploit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=PPPWN, menu=self.exploit_menu)
        self.exploit_menu.add_command(label="  Start PPPwn > ", command=self.start_pppwn)

        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)

        # Menu déroulant pour les interfaces réseau
        self.interface_var = tk.StringVar(master)
        if sys.platform == "linux":
            self.interface_var.set("Select an interface :") # Réseau pré-sélectionné
        else:
            self.interface_var.set("Ethernet")
        self.interface_menu = tk.OptionMenu(master, self.interface_var, *get_network_interface_names())
        self.interface_menu.pack()

        # Frame pour les boutons radio "PPPwn" et "PPPwn Goldhen/PS4HEN VTX"
        self.radio_frame = tk.Frame(master)
        self.radio_frame.pack()

        # Variables pour les boutons radio PPPwn et PPPwn PS4HEN
        self.selected_tab = GOLDHEN
        self.radio_var = tk.StringVar(master, value=self.selected_tab)

        # Création des boutons radio pour PPPwn, PPPwn PS4HEN, PPPwn Linux et Custom Payloads
        self.pppwn_radio_button = tk.Radiobutton(self.radio_frame, text=PPPWN, variable=self.radio_var, value=PPPWN, command=self.update_firmware_options)
        self.pppwn_radio_button.pack(side=tk.LEFT, padx=5)

        self.goldhen_radio_button = tk.Radiobutton(self.radio_frame, text=GOLDHEN, variable=self.radio_var, value=GOLDHEN, command=self.update_firmware_options)
        self.goldhen_radio_button.pack(side=tk.LEFT, padx=5)

        self.ps4hen_radio_button = tk.Radiobutton(self.radio_frame, text=PS4HEN, variable=self.radio_var, value=PS4HEN, command=self.update_firmware_options)
        self.ps4hen_radio_button.pack(side=tk.LEFT, padx=5)

        self.linux_radio_button = tk.Radiobutton(self.radio_frame, text=LINUX, variable=self.radio_var, value=LINUX, command=self.update_firmware_options)
        self.linux_radio_button.pack(side=tk.LEFT, padx=5)

        self.custom_radio_button = tk.Radiobutton(self.radio_frame, text=CUSTOM, variable=self.radio_var, value=CUSTOM, command=self.update_firmware_options)
        self.custom_radio_button.pack(side=tk.LEFT, padx=5)

        # Conteneur pour les colonnes des firmwares
        self.firmware_label = tk.Label(master, text="Choose your Firmware:")
        self.firmware_label.pack()
        self.columns_container = tk.Frame(master)
        self.columns_container.pack()

        self.selected_fw1 = "11.00"
        self.selected_fw2 = GOLDHEN_1100
        self.selected_fw3 = VTX_1100
        self.selected_fw4 = LINUX_4GB

        # Firmwares avec noms des versions
        self.firmware_var = tk.StringVar(master)
        self.firmware_var.set(self.selected_fw2)  # Firmware pré-sélectionné

        # Sélection payloads
        self.payload_frame = tk.Frame(master)

        self.payload_label = tk.Label(self.payload_frame, text="Select Payloads:")
        self.payload_label.pack()

        self.payload_var = tk.StringVar(master)

        self.custom_payloads_frame = tk.Frame(master)

        self.stage1_label = tk.Label(self.custom_payloads_frame, text="Custom Stage 1:")
        self.stage1_label.grid(row=0, column=0)

        self.stage1_path = tk.StringVar()
        self.stage1_entry = tk.Entry(self.custom_payloads_frame, textvariable=self.stage1_path, width=30)
        self.stage1_entry.grid(row=0, column=1)

        self.stage1_browse_button = tk.Button(self.custom_payloads_frame, text="Browse", command=self.select_stage1_file)
        self.stage1_browse_button.grid(row=0, column=2, padx=5)

        self.stage2_label = tk.Label(self.custom_payloads_frame, text="Custom Stage 2:")
        self.stage2_label.grid(row=1, column=0)

        self.stage2_path = tk.StringVar()
        self.stage2_entry = tk.Entry(self.custom_payloads_frame, textvariable=self.stage2_path, width=30)
        self.stage2_entry.grid(row=1, column=1)

        self.stage2_browse_button = tk.Button(self.custom_payloads_frame, text="Browse", command=self.select_stage2_file)
        self.stage2_browse_button.grid(row=1, column=2, padx=5)

        # Start PPPwn
        self.start_button = tk.Button(master, text="  Start PPPwn > ", bg='white',fg='blue', font = ('Sans','12','bold'), command=self.start_pppwn, default="active")
        self.start_button.pack(side=tk.BOTTOM, pady=10)
        self.start_button.focus()

        self.read_last_options()
        self.update_firmware_options()  # Mettre à jour les options de firmware initiales

    def update_firmware_options(self):
        # Supprimer les boutons radio actuels
        for widget in self.columns_container.winfo_children():
            widget.destroy()

        # Mettre à jour les options de firmware en fonction de la sélection de l'utilisateur
        firmware_versions = self.get_firmware_options()

        # Mémoriser la dernière option sélectionnée
        if self.selected_tab == PPPWN:
            self.selected_fw1 = self.firmware_var.get()
        elif self.selected_tab == GOLDHEN:
            self.selected_fw2 = self.firmware_var.get()
        elif self.selected_tab == PS4HEN:
            self.selected_fw3 = self.firmware_var.get()
        elif self.selected_tab == LINUX:
            self.selected_fw4 = self.firmware_var.get()
        elif self.selected_tab == CUSTOM:
            self.custom_payloads_frame.pack_forget() # Supprimer les boutons personnalisés

        # Créer les colonnes des boutons radio avec les nouvelles options de firmware
        if self.radio_var.get() == PPPWN:
            num_columns = 3
            self.selected_tab = PPPWN
            self.firmware_var.set(self.selected_fw1)
        elif self.radio_var.get() == GOLDHEN:
            num_columns = 2
            self.selected_tab = GOLDHEN
            self.firmware_var.set(self.selected_fw2)
        elif self.radio_var.get() == PS4HEN:
            num_columns = 2
            self.selected_tab = PS4HEN
            self.firmware_var.set(self.selected_fw3)
        elif self.radio_var.get() == LINUX:
            num_columns = 1
            self.selected_tab = LINUX
            self.firmware_var.set(self.selected_fw4)
        elif self.radio_var.get() == CUSTOM:
            num_columns = 2
            self.selected_tab = CUSTOM
            self.firmware_var.set(CUSTOM)
            self.custom_payloads_frame.pack() # Créer les boutons personnalisés

        column_widgets = []
        if self.radio_var.get() == CUSTOM:
            no_label = tk.Label(self.columns_container, text="")
            column_widgets.append(no_label)
        else:
            for firmware in firmware_versions:
               radio_button = tk.Radiobutton(self.columns_container, text=firmware, variable=self.firmware_var, value=firmware, command=self.show_payload_options)
               column_widgets.append(radio_button)
    
        for i, widget in enumerate(column_widgets):
            column_index = i % num_columns
            row_index = i // num_columns
            widget.grid(row=row_index, column=column_index, sticky="w")

        self.show_payload_options

    def get_firmware_options(self):
        if self.radio_var.get() == PPPWN:
            # Options de firmware pour PPPwn
            return ["7.00", "7.01", "7.02", "7.50", "7.51", "7.55",
                    "8.00", "8.01", "8.03", "8.50", "8.52",
                    "9.00", "9.03", "9.04", "9.50", "9.51", "9.60",
                    "10.00", "10.01", "10.50", "10.70", "10.71", "11.00"]
        elif self.radio_var.get() == GOLDHEN:
            # Options de firmware pour PPPwn PS4HEN
            return [GOLDHEN_900, GOLDHEN_950, GOLDHEN_951, GOLDHEN_960,
                    GOLDHEN_1000, GOLDHEN_1001,
                    GOLDHEN_1050, GOLDHEN_1070, GOLDHEN_1071, GOLDHEN_1100]
        elif self.radio_var.get() == PS4HEN:
            # Options de firmware pour PPPwn PS4HEN
            return [VTX_800, VTX_803, VTX_850, VTX_852, VTX_903, VTX_904, VTX_1000, VTX_1001, VTX_1050, VTX_1070, VTX_1071, VTX_1100]
        elif self.radio_var.get() == LINUX:
            # Options de firmware pour PPPwn Linux
            return [LINUX_1GB, LINUX_2GB, LINUX_3GB, LINUX_4GB]
        elif self.radio_var.get() == CUSTOM:
            # Options de firmware pour Custom Payloads
            return [CUSTOM]

    def show_payload_options(self):
        if self.firmware_var.get() == CUSTOM:
            self.payload_frame.pack()
            self.custom_payloads_frame.pack()
        else:
            self.payload_frame.pack_forget()
            self.custom_payloads_frame.pack_forget()

    def select_stage1_file(self):
        stage1_file = filedialog.askopenfilename()
        self.stage1_path.set(stage1_file)

    def select_stage2_file(self):
        stage2_file = filedialog.askopenfilename()
        self.stage2_path.set(stage2_file)

    def read_line(self, f):
        return f.readline().replace('\n','')

    def read_last_options(self):
        if os.path.isfile("PPPwnUI.dat"):
            f = open("PPPwnUI.dat", "r")
            self.interface_var.set(self.read_line(f))
            self.selected_tab = self.read_line(f)
            self.radio_var.set(self.selected_tab)
            self.selected_fw1 = self.read_line(f)
            self.selected_fw2 = self.read_line(f)
            self.selected_fw3 = self.read_line(f)
            self.selected_fw4 = self.read_line(f)
            self.stage1_path.set(self.read_line(f))
            self.stage2_path.set(self.read_line(f))
            self.firmware_var.set(self.read_line(f))
            f.close()

    def save_last_options(self, interface, firmware):
        f = open("PPPwnUI.dat", "w")
        f.write(interface + '\n')
        f.write(self.selected_tab + '\n')
        f.write(self.selected_fw1 + '\n')
        f.write(self.selected_fw2 + '\n')
        f.write(self.selected_fw3 + '\n')
        f.write(self.selected_fw4 + '\n')
        f.write(self.stage1_path.get() + '\n')
        f.write(self.stage2_path.get() + '\n')
        f.write(firmware + '\n')
        f.close()

    def button_click(self, event):
        self.start_pppwn()

    def start_pppwn(self):
        interface = self.interface_var.get()
        firmware = self.firmware_var.get()

        stage1_path = self.stage1_path.get()
        stage2_path = self.stage2_path.get()

        if interface == "Select an interface :":
            messagebox.showerror("Error", "Select a network interface")
            return

        self.save_last_options(interface, firmware)

        if firmware == CUSTOM:
            firmware_value = self.selected_fw1.replace(".", "")
            if os.path.isfile(stage1_path) == False:
                messagebox.showerror("Error", "stage1 does not exist")
                return
            if os.path.isfile(stage2_path) == False:
                messagebox.showerror("Error", "stage2 does not exist")
                return
            command = f'PPPwn/pppwn.py --interface="{interface}" --fw="{firmware_value}" --stage1="{stage1_path}" --stage2="{stage2_path}"'
        elif firmware.find("Linux ") != -1:
            firmware_value = firmware[-5:]
            size_gb = firmware.replace("Linux ","").replace("GB " + firmware_value, "")
            firmware_value = firmware_value.replace(".", "")
            command = f'PPPwn/pppwn.py --interface="{interface}" --fw="{firmware_value}" --stage1="PPPwn/Linux/{firmware_value}/stage1.bin" --stage2="PPPwn/Linux/{firmware_value}/stage2-{size_gb}gb.bin"'
        elif firmware.find("VTX HEN for ") != -1:
            firmware_value = firmware.replace("VTX HEN for ","").replace(".", "")
            command = f'PPPwn/pppwn.py --interface="{interface}" --fw="{firmware_value}" --stage1="PPPwn/vtx/{firmware_value}/stage1.bin" --stage2="PPPwn/vtx/{firmware_value}/stage2.bin"'
        elif firmware.find("Goldhen for ") != -1:
            firmware_value = firmware.replace("Goldhen for ","").replace(".", "")
            command = f'PPPwn/pppwn.py --interface="{interface}" --fw="{firmware_value}" --stage1="PPPwn/goldhen/{firmware_value}/stage1.bin" --stage2="PPPwn/goldhen/{firmware_value}/stage2.bin"'
        else:
            firmware_value = firmware.replace(".", "")
            if firmware_value.isdigit():
                command = f'PPPwn/pppwn.py --interface="{interface}" --fw="{firmware_value}" --stage1="PPPwn/stage1/{firmware_value}/stage1.bin" --stage2="PPPwn/stage2/{firmware_value}/stage2.bin"'
            else:
                messagebox.showerror("Error", "Invalid firmware selection")
                return

        try:
            if sys.platform == "linux":
                subprocess.Popen(f'python3 ' + command, shell=True)
            else:
                subprocess.Popen(f'python ' + command, shell=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def about(self):
        messagebox.showinfo("About", "PPPwnUI v3.0 by Memz (mod by aldostools)\nThis app was originally developed by Memz to make PPPwn easier to use.")

if sys.platform == "linux" and not os.geteuid() == 0:
    print("You must run this program as administrator.")
    sys.exit(1)

root = tk.Tk()
app = App(root)
root.mainloop()