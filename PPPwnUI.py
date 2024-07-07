import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox, filedialog, Canvas, PhotoImage
from urllib.request import urlretrieve
import psutil
import subprocess
import tempfile
import os
import sys
import ctypes
import shutil

GUI_VERSION = "3.25a+"
hen_version = "1.0309"
destination_path = "USB Drive (GoldHEN_v2.4b17.3)"

# Tabs
PPPWN   = "PPPwn"
GOLDHEN = "GOLDHEN"
PS4HEN  = "PS4HEN VTX"
NOBD    = "PS4HEN NOBD" # PS4HEN VTX also supports NOBD
LINUX   = "Linux"
CUSTOM  = "Custom"

# GOLDHEN Options
GOLDHEN_900 = "Goldhen for 9.00"
GOLDHEN_950 = "Goldhen for 9.50"
GOLDHEN_951 = "Goldhen for 9.51"
GOLDHEN_960 = "Goldhen for 9.60"
GOLDHEN_1000 = "Goldhen for 10.00"
GOLDHEN_1001 = "Goldhen for 10.01"
GOLDHEN_1050 = "Goldhen for 10.50" # Not supported yet
GOLDHEN_1070 = "Goldhen for 10.70" # Not supported yet
GOLDHEN_1071 = "Goldhen for 10.71" # Not supported yet
GOLDHEN_1100 = "Goldhen for 11.00"

# PS4HEN VTX + USB BinLoader Options
PS4HEN_700  = "payload.bin for 7.00"
PS4HEN_701  = "payload.bin for 7.01"
PS4HEN_702  = "payload.bin for 7.02"
PS4HEN_750  = "payload.bin for 7.50"
PS4HEN_751  = "payload.bin for 7.51"
PS4HEN_755  = "payload.bin for 7.55"
PS4HEN_800  = "payload.bin for 8.00"
PS4HEN_801  = "payload.bin for 8.01"
PS4HEN_803  = "payload.bin for 8.03"
PS4HEN_850  = "payload.bin for 8.50"
PS4HEN_852  = "payload.bin for 8.52"
PS4HEN_900  = "payload.bin for 9.00"
PS4HEN_903  = "payload.bin for 9.03"
PS4HEN_904  = "payload.bin for 9.04"
PS4HEN_950  = "payload.bin for 9.50"
PS4HEN_951  = "payload.bin for 9.51"
PS4HEN_960  = "payload.bin for 9.60"
PS4HEN_1000 = "payload.bin for 10.00"
PS4HEN_1001 = "payload.bin for 10.01"
PS4HEN_1050 = "payload.bin for 10.50"
PS4HEN_1070 = "payload.bin for 10.70"
PS4HEN_1071 = "payload.bin for 10.71"
PS4HEN_1100 = "payload.bin for 11.00"

# Linux Options
LINUX_1GB = "Linux 1GB 11.00"
LINUX_2GB = "Linux 2GB 11.00"
LINUX_3GB = "Linux 3GB 11.00"
LINUX_4GB = "Linux 4GB 11.00"

done_file = "done.bat"
retry_file = "PPPwn/retry"

if sys.platform == "win32":
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32
    
def create_file(filepath):
    f = open(filepath, "w")
    f.close()

def remove_file(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)

def get_network_interface_names():
    interfaces = psutil.net_if_addrs()
    return interfaces.keys()

class App:
    def __init__(self, window):
        self.window = window
        window.title("PPPwnUI v" + GUI_VERSION + " by Memz (mod by aldostools)")

        # Set the resizable property False
        window.resizable(False, False)

        # Center the window
        window_width = 580
        window_height = 460

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # logo d'application
        if sys.platform == "linux":
            pass
        else :
            window.iconbitmap("media/logo.ico")

        self.menu = tk.Menu(window)
        window.config(menu=self.menu)
        window.bind('<Return>', self.button_click)
        window.bind('<Escape>', self.window_exit)
        window.bind('<Control-s>', self.save_settings)

        self.hwnd = 0
        self.allow_hide = False

        if sys.platform == "win32":
            # Hide Console
            self.hwnd = kernel32.GetConsoleWindow()
            user32.ShowWindow(self.hwnd, 0)

            # Hide Console Title
            GWL_STYLE = -16
            WS_BORDER = 0x00800000 # window with border
            WS_DLGFRAME = 0x00400000 # window with double border but no title
            WS_CAPTION = WS_BORDER | WS_DLGFRAME # window with a title bar

            style = user32.GetWindowLongW(self.hwnd, GWL_STYLE);
            user32.SetWindowLongW(self.hwnd, GWL_STYLE, (style & ~WS_CAPTION));

            # Set Console Title
            user32.SetWindowTextW(self.hwnd, "PPPwnUI v" + GUI_VERSION)

            # Move & Resize Console
            user32.MoveWindow(self.hwnd, window.winfo_x(), window.winfo_y() + 160, window_width + 16, 300, 1)

            # Disable Console Resize
            MF_BYCOMMAND = 0x00000000
            SC_MINIMIZE = 0xF020
            SC_MAXIMIZE = 0xF030
            SC_SIZE = 0xF000

            sysMenu = user32.GetSystemMenu(self.hwnd, False)
            user32.DeleteMenu(sysMenu, SC_MINIMIZE, MF_BYCOMMAND)
            user32.DeleteMenu(sysMenu, SC_MAXIMIZE, MF_BYCOMMAND)
            user32.DeleteMenu(sysMenu, SC_SIZE, MF_BYCOMMAND)

            # Change Default Font
            self.defaultFont = font.nametofont("TkDefaultFont") 
            self.defaultFont.configure(family="Tahoma", size=10)

            # Hide console window on click & on move / click title
            window.bind('<Button-1>', self.hide_console)
            window.bind('<Configure>', self.hide_console)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save       Ctrl+S", command=self.save_last_options)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit         Esc", command=self.menu_exit)

        self.retry_var = tk.StringVar(window)
        self.retry_var.set("1")

        self.runbat_var = tk.StringVar(window)
        self.runbat_var.set("1")

        self.tool_var = tk.StringVar(window)
        self.tool_var.set("0")

        self.exploit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=PPPWN, menu=self.exploit_menu)
        self.exploit_menu.add_checkbutton(label=f"  Retry PPPwn ", onvalue="1", offvalue="0", variable=self.retry_var)
        self.exploit_menu.add_checkbutton(label=f"  Run {done_file} & Exit when done ", onvalue="1", offvalue="0", variable=self.runbat_var)
        if sys.platform == "win32":
            self.exploit_menu.add_command(label="  Show Console ", command=self.show_console)
        self.exploit_menu.add_separator()
        self.exploit_menu.add_command(label="  Start PPPwn > ", command=self.start_pppwn, font = ('Sans','12','bold'))

        self.tool_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Tool", menu=self.tool_menu)
        self.tool_menu.add_radiobutton(label="  PPPwn.py ",  value="0", variable=self.tool_var)
        self.tool_menu.add_radiobutton(label="  PPPwn GO ",  value="1", variable=self.tool_var)
        self.tool_menu.add_radiobutton(label="  PPPwn C++ ", value="2", variable=self.tool_var)

        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Download PPPwnUI", command=self.download_update)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="About", command=self.about)

        self.image = tk.PhotoImage(file="media/logo.png")
        self.label = ttk.Label(image=self.image)
        self.label.pack(side=tk.TOP, padx=5)
        if sys.platform == "win32":
            self.label.bind('<Button-1>', self.image_click)

        # Menu déroulant pour les interfaces réseau
        self.interface_var = tk.StringVar(window)
        if sys.platform == "linux":
            self.interface_var.set("Select an interface :") # Réseau pré-sélectionné
        else:
            self.interface_var.set("Ethernet")
        self.interface_menu = tk.OptionMenu(window, self.interface_var, *get_network_interface_names())
        self.interface_menu.pack()

        # Frame pour les boutons radio "PPPwn" et "PPPwn Goldhen/PS4HEN VTX"
        self.radio_frame = tk.Frame(window)
        self.radio_frame.pack()

        # Variables pour les boutons radio PPPwn et PPPwn PS4HEN
        self.selected_tab = GOLDHEN
        self.radio_var = tk.StringVar(window, value=self.selected_tab)

        tabs = [PPPWN, GOLDHEN, PS4HEN, NOBD, LINUX, CUSTOM ]

        # Création des boutons radio pour PPPwn, PPPwn PS4HEN, PPPwn Linux et Custom Payloads
        self.radios = []
        for option in tabs:
            radio = tk.Radiobutton(self.radio_frame, text = '  ' + option + '  ', 
                                   value = option, variable = self.radio_var, indicator = 0,
                                   command=self.update_firmware_options,
                                   background = "white",
                                   font = ('Sans','11', font.BOLD))
            self.radios.append(radio)
            radio.pack(side=tk.LEFT, padx=0)

        # Conteneur pour les colonnes des firmwares
        self.firmware_label = tk.Label(window, text="Choose your Firmware:", pady=5)
        self.firmware_label.pack()
        self.columns_container = tk.Frame(window)
        self.columns_container.pack()

        self.selected_fw1 = "11.00"
        self.selected_fw2 = GOLDHEN_1100
        self.selected_fw3 = PS4HEN_1100
        self.selected_fw4 = PS4HEN_1100
        self.selected_fw5 = LINUX_4GB

        # Firmwares avec noms des versions
        self.firmware_var = tk.StringVar(window)
        self.firmware_var.set(self.selected_fw2)  # Firmware pré-sélectionné

        # Sélection payloads
        self.payload_frame = tk.Frame(window)

        self.payload_label = tk.Label(self.payload_frame, text="Select Payloads:")
        self.payload_label.pack()

        self.payload_var = tk.StringVar(window)

        self.custom_payloads_frame = tk.Frame(window)

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
        self.start_button = tk.Button(window, text="  Start PPPwn > ", bg='white',fg='blue', font = ('Sans','12','bold'), command=self.start_pppwn, default="active")
        self.start_button.pack(side=tk.BOTTOM, pady=5)
        self.start_button.focus()

        self.autostart_var = tk.StringVar(window)
        self.autostart_var.set("0")
        self.autostart_checkbox = tk.Checkbutton(window, text='Auto Start',variable=self.autostart_var, onvalue=1, offvalue=0, fg='gray', font = ('Sans','8'))
        self.autostart_checkbox.pack(side=tk.BOTTOM)

        self.read_last_options()
        self.update_firmware_options()  # Mettre à jour les options de firmware initiales
        window.update()

        if self.autostart_var.get() == "1":
            self.start_pppwn()

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
        elif self.selected_tab == NOBD:
            self.selected_fw4 = self.firmware_var.get()
        elif self.selected_tab == LINUX:
            self.selected_fw5 = self.firmware_var.get()
        elif self.selected_tab == CUSTOM:
            self.custom_payloads_frame.pack_forget() # Supprimer les boutons personnalisés

        # hilight current option
        current_tab = self.radio_var.get()
        for radio in self.radios:
            radio.configure(foreground = "blue" if radio.cget('value') == current_tab else "black")

        # Créer les colonnes des boutons radio avec les nouvelles options de firmware
        if current_tab == PPPWN:
            num_columns = 3
            self.selected_tab = PPPWN
            self.firmware_var.set(self.selected_fw1)
        elif current_tab == GOLDHEN:
            num_columns = 2
            self.selected_tab = GOLDHEN
            self.firmware_var.set(self.selected_fw2)
        elif current_tab == PS4HEN:
            num_columns = 3
            self.selected_tab = PS4HEN
            self.firmware_var.set(self.selected_fw3)
        elif current_tab == NOBD:
            num_columns = 3
            self.selected_tab = NOBD
            self.firmware_var.set(self.selected_fw4)
        elif current_tab == LINUX:
            num_columns = 1
            self.selected_tab = LINUX
            self.firmware_var.set(self.selected_fw5)
        elif current_tab == CUSTOM:
            num_columns = 2
            self.selected_tab = CUSTOM
            self.firmware_var.set(CUSTOM)
            self.custom_payloads_frame.pack() # Créer les boutons personnalisés

        column_widgets = []
        if current_tab == CUSTOM:
            no_label = tk.Label(self.columns_container, text="")
            column_widgets.append(no_label)
        else:
            for firmware in firmware_versions:
               if firmware == "":
                   no_label = tk.Label(self.columns_container, text="")
                   column_widgets.append(no_label)
               else:
                   radio_button = tk.Radiobutton(self.columns_container, text=firmware, variable=self.firmware_var, value=firmware, command=self.show_payload_options)
                   column_widgets.append(radio_button)

        for i, widget in enumerate(column_widgets):
            column_index = i % num_columns
            row_index = i // num_columns
            widget.grid(row=row_index, column=column_index, sticky="w")

        self.show_payload_options

    def get_firmware_options(self):
        current_tab = self.radio_var.get()
        if current_tab == PPPWN:
            # Options de firmware pour PPPwn
            return ["7.00", "7.01", "7.02", "7.50", "7.51", "7.55",
                    "8.00", "8.01", "8.03", "8.50", "8.52",
                    "9.00", "9.03", "9.04", "9.50", "9.51", "9.60",
                    "10.00", "10.01", "10.50", "10.70", "10.71", "11.00"]
        elif current_tab == GOLDHEN:
            # Options de firmware pour PPPwn PS4HEN
            return [GOLDHEN_900,
                    GOLDHEN_950, GOLDHEN_951, GOLDHEN_960,
                    GOLDHEN_1000, GOLDHEN_1001,
                  # GOLDHEN_1050, GOLDHEN_1070, GOLDHEN_1071,
                    GOLDHEN_1100]
        elif current_tab == PS4HEN or current_tab == NOBD:
            # Options de firmware pour PS4HEN VTX + USB BinLoader
            return [PS4HEN_700, PS4HEN_701, PS4HEN_702, PS4HEN_750, PS4HEN_751, PS4HEN_755,
                    PS4HEN_800, PS4HEN_801, PS4HEN_803, PS4HEN_850, PS4HEN_852, "",
                    PS4HEN_900, PS4HEN_903, PS4HEN_904, PS4HEN_950, PS4HEN_951, PS4HEN_960,
                    PS4HEN_1000, PS4HEN_1001, PS4HEN_1050, PS4HEN_1070, PS4HEN_1071,
                    PS4HEN_1100]
        elif current_tab == LINUX:
            # Options de firmware pour PPPwn Linux
            return [LINUX_1GB, LINUX_2GB, LINUX_3GB, LINUX_4GB]
        elif current_tab == CUSTOM:
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
            if self.read_line(f).find("UI Version: +") == 0:
               self.interface_var.set(self.read_line(f))
               self.selected_tab = self.read_line(f)
               self.radio_var.set(self.selected_tab)
               self.selected_fw1 = self.read_line(f)
               self.selected_fw2 = self.read_line(f)
               self.selected_fw3 = self.read_line(f)
               self.selected_fw4 = self.read_line(f).replace("NOBD ", "")
               self.selected_fw5 = self.read_line(f)
               self.stage1_path.set(self.read_line(f))
               self.stage2_path.set(self.read_line(f))
               self.firmware_var.set(self.read_line(f).replace("NOBD ", ""))
               self.autostart_var.set(self.read_line(f))
               self.retry_var.set(self.read_line(f))
               self.runbat_var.set(self.read_line(f))
               self.tool_var.set(self.read_line(f))
            f.close()

    def save_last_options(self):
        f = open("PPPwnUI.dat", "w")
        f.write("UI Version: +" + GUI_VERSION + '\n')
        f.write(self.interface_var.get() + '\n')
        f.write(self.selected_tab + '\n')
        f.write(self.selected_fw1 + '\n')
        f.write(self.selected_fw2 + '\n')
        f.write(self.selected_fw3 + '\n')
        f.write(self.selected_fw4 + '\n')
        f.write(self.selected_fw5 + '\n')
        f.write(self.stage1_path.get() + '\n')
        f.write(self.stage2_path.get() + '\n')
        f.write(self.firmware_var.get() + '\n')
        f.write(self.autostart_var.get() + '\n')
        f.write(self.retry_var.get() + '\n')
        f.write(self.runbat_var.get() + '\n')
        f.write(self.tool_var.get() + '\n')
        f.close()

    def menu_exit(self):
        remove_file(retry_file)
        self.window.quit()

    def window_exit(self, event):
        self.menu_exit()

    def button_click(self, event):
        self.start_pppwn()

    def save_settings(self, event):
        self.save_last_options()

    #### Windows functions
    def create_reset_network_script(self):
        interface = self.interface_var.get()
        f = open("ResetNetwork.bat", "w")
        f.write(f'@netsh interface set interface "{interface}" disable && echo {interface} resetted\n')
        f.write(f'@netsh interface set interface "{interface}" enable\n')
        f.write(f'@pause\n')
        f.close()

    def show_console(self):
        user32.MoveWindow(self.hwnd, root.winfo_x(), root.winfo_y() + 160, root.winfo_width() + 16, 300, 1)
        user32.ShowWindow(self.hwnd, 5)
        user32.SetForegroundWindow(self.hwnd)
        self.create_reset_network_script()

    def hide_console(self, event):
        if self.allow_hide:
            user32.ShowWindow(self.hwnd, 0)
        self.allow_hide = True

    def image_click(self, event):
        self.allow_hide = False
        self.show_console()
    ####

    def clear_console(self):
        if sys.platform == "linux":
            os.system('clear')
        else:
            os.system('cls')

    def get_netid_from_list(self, interface):
        # use first term in interface name for match
        name = interface.partition(' ')[0].lower()

        if sys.platform == "linux":
            program = './PPPwn/pppwn_cpp list'
        else:
            program = 'PPPwn\\pppwn_cpp.exe list'

        with tempfile.TemporaryFile() as stdout:
            # get interface list
            proc = subprocess.Popen(program, stdout=stdout).wait()
            stdout.seek(0)
            lines = stdout.read()
            
            # find interface name in list
            for line in lines.splitlines():
                line = str(line).replace('\\\\','\\').partition(' ')
                if line[2].lower().find(name) >= 0:
                    # print interface name
                    print(line[2])
                    # return interface id
                    return line[0][4:]
            # print interface name
            self.clear_console()
            print(line[2])
            # return interface id
            return line[0][4:]

    def start_pppwn(self):
        # Get parameters
        interface = self.interface_var.get()
        firmware = self.firmware_var.get()

        # Check network interface
        if interface == "Select an interface :":
            messagebox.showerror("Error", "Select a network interface")
            return

        # Get firmware version and set parameters
        if firmware == CUSTOM:
            firmware_value = self.selected_fw1.replace(".", "")
            stage1_path = self.stage1_path.get()
            stage2_path = self.stage2_path.get()
            command = f'--fw="{firmware_value}" --stage1="{stage1_path}" --stage2="{stage2_path}"'
        elif firmware.find("Goldhen for ") != -1:
            firmware_value = firmware.replace("Goldhen for ","").replace(".", "")
            command = f'--fw="{firmware_value}" --stage1="PPPwn/stage1/{firmware_value}/stage1.bin" --stage2="PPPwn/goldhen/{firmware_value}/stage2.bin"'
        elif firmware.find("payload.bin for ") != -1:
            firmware_value = firmware.replace("payload.bin for ","").replace(".", "")
            command = f'--fw="{firmware_value}" --stage1="PPPwn/stage1/{firmware_value}/stage1.bin" --stage2="PPPwn/ps4hen/{firmware_value}/stage2.bin"'
        elif firmware.find("Linux ") != -1:
            firmware_value = firmware[-5:]
            size_gb = firmware.replace("Linux ","").replace("GB " + firmware_value, "")
            firmware_value = firmware_value.replace(".", "")
            command = f'--fw="{firmware_value}" --stage1="PPPwn/Linux/{firmware_value}/stage1.bin" --stage2="PPPwn/Linux/{firmware_value}/stage2-{size_gb}gb.bin"'
        else:
            firmware_value = firmware.replace(".", "")
            if firmware_value.isdigit():
                command = f'--fw="{firmware_value}" --stage1="PPPwn/stage1/{firmware_value}/stage1.bin" --stage2="PPPwn/stage2/{firmware_value}/stage2.bin"'
            else:
                messagebox.showerror("Error", "Invalid firmware selection")
                return

        # Check stage1 exists
        stage1_path = command.split('"')[1::2][1]
        if os.path.isfile(stage1_path) == False:
            messagebox.showerror("Error", "stage1 does not exist")
            return

        # Check stage2 exists
        stage2_path = command.split('"')[1::2][2]
        if os.path.isfile(stage2_path) == False:
            messagebox.showerror("Error", "stage2 does not exist")
            return

        # Get program path
        if sys.platform == "linux":
            if self.tool_var.get() == "1":
                program = './PPPwn/pppwn_go '
            elif self.tool_var.get() == "2":
                program = f'./PPPwn/pppwn_cpp --interface {interface} '
                command = command.replace("=", " ")
            else:
                program = f'python3 PPPwn/pppwn.py --interface="{interface}" '
        else:
            if self.tool_var.get() == "1":
                program = 'PPPwn\\pppwn_go.exe '
            elif self.tool_var.get() == "2":
                interface = self.get_netid_from_list(interface)
                program = f'PPPwn\\pppwn_cpp.exe --interface {interface} '
                command = command.replace("=", " ")
            else:
                program = f'python PPPwn/pppwn.py --interface="{interface}" '

        # Save settings
        self.save_last_options()

        # Show clear console
        if sys.platform == "win32":
            self.show_console()
        self.clear_console()

        # Copy payload.bin for PS4HEN
        if firmware.find("payload.bin for ") != -1:
            source_payload = f"./{destination_path}/payloads/ps4-hen-{firmware_value}-PPPwn-{hen_version}.bin"
            if os.path.isfile(source_payload) and os.path.isdir(destination_path):
                shutil.copy(source_payload, destination_path + "/payload.bin")

        # Get setting for done.bat & quit GUI
        runbat = (self.runbat_var.get() == "1" and os.path.isfile(done_file))

        # PPPwn
        if (runbat == True or self.retry_var.get() == "1") and self.tool_var.get() == "0":
            # Run PPPwn.py and wait until payload is done (keep trying)
            create_file(retry_file)
            while(os.path.isfile(retry_file)):
                try:
                    subprocess.Popen(program + command, shell=True).wait()
                except subprocess.CalledProcessError as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")
                    return
                if self.retry_var.get() == "0":
                    if os.path.isfile(retry_file):
                        return
        else:
            # Run PPPwn and wait until payload is done
            remove_file(retry_file)
            try:
                if runbat == True and self.tool_var.get() >= "1":
                    subprocess.Popen(program + command, shell=True).wait() # wait for PPPwn_GO or PPPwn_CPP
                else:
                    subprocess.Popen(program + command, shell=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        # Quit GUI
        if(runbat == True):
            if sys.platform == "linux":
                subprocess.Popen('./' + done_file, shell=True)
            else:
                subprocess.Popen(done_file, shell=True)
            self.menu_exit()

    def download_update(self):
        urlretrieve("https://github.com/aldostools/PPPwnUI/archive/refs/heads/main.zip", "PPPwnUI.zip")
        if sys.platform == "win32":
            subprocess.Popen('explorer "PPPwnUI.zip"')

    def about(self):
        messagebox.showinfo("About", "PPPwnUI v" + GUI_VERSION + " by Memz (mod by aldostools)\n" +
                            "This app was originally developed by Memz to make PPPwn easier to use.\n\n" +
                             "PPPwn by Andy Nguyen (TheFlow)\n" +
                             destination_path[destination_path.find("(")+1:destination_path.find(")")] + " by SiSTR0\n" +
                             "PS4HEN PPPwn VTX v" + hen_version + " by EchoStretch & BestPig\n" +
                             "Special thanks to LightningMods, EinTim23, Memz")

if sys.platform == "linux" and not os.geteuid() == 0:
    print("You must run this program as administrator.")
    sys.exit(1)

root = tk.Tk()
app = App(root)
root.mainloop()