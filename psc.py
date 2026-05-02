import tkinter as tk
from tkinter import messagebox
import subprocess
import pkg_resources
import webbrowser
import re
import secrets
import string
import hashlib
import requests
from PIL import Image, ImageTk
import tempfile, os


# Ensure required packages are installed
required_packages = ['zxcvbn', 'requests']
for package in required_packages:
    try:
        pkg_resources.get_distribution(package)
    except pkg_resources.DistributionNotFound:
        subprocess.check_call(['pip', 'install', package])

from zxcvbn import zxcvbn

def project_info():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Project Information</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: #fff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                position: relative;
            }
            .logo {
                position: absolute;
                top: 20px;
                right: 20px;
            }
            .logo img {
                height: 80px;
                width: auto;
            }
            h1 {
                color: #d9534f;
                text-align: center;
                margin-bottom: 20px;
            }
            p {
                line-height: 1.6;
                margin-bottom: 10px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #d9534f;
                color: white;
            }
            a {
                color: #d9534f;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                font-size: 0.9em;
                color: #777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">
               <img src="data:image/jpeg;base64,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" alt="Company Logo" style="height:80px;">

            </div>
            <h1>Project Information</h1>
            <p>This project was developed as part of a <strong>Cyber Security Internship</strong>. This project is designed to <strong>Secure the Organizations in Real World from Cyber Frauds performed by Hackers</strong>.</p>
            <table>
                <tr><th>Project Details</th><th>Value</th></tr>
                <tr><td>Project Name</td><td>Password Strength Checker</td></tr>
                <tr><td>Project Description</td><td>Developing Password Strength Checker to know the Strength of the Passwords to avoid Cyber Attacks</td></tr>
                <tr><td>Project Start Date</td><td>10-JULY-2025</td></tr>
                <tr><td>Project End Date</td><td>5-AUG-2025</td></tr>
                <tr><td>Project Status</td><td><strong>Completed</strong></td></tr>
            </table>

            <h2>Developer Details</h2>
            <table>
                <tr><th>Name</th><th>Employee ID</th><th>Email</th></tr>
                <tr><td>Kathera Bhavita</td><td>ST#IS#7443</td><td>katherabhavita2308@gamil.com</td></tr>
                <tr><td>Nireekhana Chinthaginjala</td><td>ST#IS#7481</td><td>nireekshana0805@gmail.com</td></tr>
                <tr><td>Dappu Bhanu Charan</td><td>ST#IS#7475</td><td>dappubhanu18@gmail.com</td></tr>
                <tr><td>Saikiran Mulugu</td><td>ST#IS#7482</td><td>saikiranfor875@gmail.com</td></tr>
            </table>

            <h2>Company Details</h2>
            <table>
                <tr><th>Company</th><th>Value</th></tr>
                <tr><td>Name</td><td>Supraja Technologies</td></tr>
            </table> 

            <h2>Contact Information</h2>
            <table>
                <tr><th>Category</th><th>Details</th></tr>
                <tr><td>Email</td><td><a href="mailto:contact@suprajatechnologies.com">contact@suprajatechnologies.com</a></td></tr>
                <tr><td>Website</td><td><a href="https://www.suprajatechnologies.com" target="_blank">suprajatechnologies.com</a></td></tr>
            </table>

            <div class="footer">
                &copy; 2025 Supraja Technologies. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html', encoding='utf-8') as temp_file:
            temp_file.write(html_code)
            temp_file_path = temp_file.name
        webbrowser.open('file://' + os.path.realpath(temp_file_path))
    except Exception as e:
        messagebox.showerror("Error", f"Could not open project info: {e}")



def is_password_pwned(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1pwd[:5]
    suffix = sha1pwd[5:]
    try:
        res = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
        if res.status_code != 200:
            return -1
        hashes = (line.split(':') for line in res.text.splitlines())
        for hash_suffix, count in hashes:
            if hash_suffix == suffix:
                return int(count)
        return 0
    except Exception as e:
        print(f"Error checking data breach: {e}")
        return -1

def lookup_email_or_username(identifier):
    try:
        if re.match(r"[^@]+@[^@]+\.[^@]+", identifier):
            search_type = "email_address"
        else:
            search_type = "username"
        url = "https://leak-lookup.com/api/search"
        payload = {
            "key": "public_leak_lookup",
            "type": search_type,
            "query": identifier
        }
        res = requests.post(url, json=payload)
        if res.status_code == 200:
            return res.json()
        else:
            return {"status": "error", "message": f"HTTP {res.status_code}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def on_lookup():
    identifier = email_var.get().strip()
    if not identifier:
        messagebox.showwarning("Input Error", "Please enter an email or username to check!")
        return
    result = lookup_email_or_username(identifier)
    if result.get("status") == "error":
        messagebox.showerror("Lookup Error", result.get("message"))
    else:
        leaks = result.get("found", 0)
        message = f"🔍 Tool: Leak-Lookup.com\n\nIdentifier: {identifier}\nFound in {leaks} breaches."
        messagebox.showinfo("Lookup Result", message)

def check_password_strength(password):
    strength_window = tk.Toplevel(root)
    strength_window.title("Password Strength")
    strength_window.geometry("600x700")
    strength_window.configure(bg="black")

    tk.Label(strength_window, text=f"Your Password: {password}", font=("Arial", 12, "bold"), bg="black", fg="#ff0000").pack(pady=10)

    requirement_frame = tk.Frame(strength_window, bg="white")
    requirement_frame.pack(side="top", fill="x", padx=50, pady=10)

    time_frame = tk.Frame(strength_window, bg="white")
    time_frame.pack(side="top", fill="x", padx=50, pady=10)

    suggestion_frame = tk.Frame(strength_window, bg="white")
    suggestion_frame.pack(side="top", fill="x", padx=50, pady=10)

    all_good = True

    if len(password) < 8:
        tk.Label(requirement_frame, text="Your Password Must Contain At Least 8 Characters!!!", padx=10, pady=5, bg="white", fg="black").pack()
        all_good = False

    if not re.search("[A-Z]", password):
        tk.Label(requirement_frame, text="Your Password Must Contain At Least One Capital Letter!!!", padx=10, pady=5, bg="white", fg="black").pack()
        all_good = False

    if not re.search("[0-9]", password):
        tk.Label(requirement_frame, text="Your Password Must Contain At Least One Digit!!!", padx=10, pady=5, bg="white", fg="black").pack()
        all_good = False

    if not re.search(r"[!@#$%^&*(),.?\":{}[\]<>]", password):
        tk.Label(requirement_frame, text="Your Password Must Contain At Least One Special Character!!!", padx=10, pady=5, bg="white", fg="black").pack()
        all_good = False

    if all_good:
        tk.Label(requirement_frame, text="All Password Requirements Satisfied!!!", padx=10, pady=5, bg="white", fg="green", font=("Arial", 12, "bold")).pack()

    breach_count = is_password_pwned(password)
    if breach_count > 0:
        tk.Label(requirement_frame, text=f"This password was found in {breach_count:,} breaches!", padx=10, pady=5, bg="white", fg="red", font=("Arial", 10, "bold")).pack()
    elif breach_count == 0:
        tk.Label(requirement_frame, text="This password was NOT found in known breaches.", padx=10, pady=5, bg="white", fg="green").pack()
    else:
        tk.Label(requirement_frame, text="Could not check breach status (network error).", padx=10, pady=5, bg="white", fg="orange").pack()

    result = zxcvbn(password)
    tk.Label(time_frame, text="Estimated Crack Times:", bg="white", font=("Arial", 12, "bold")).pack(pady=5)
    for attack_type, time_str in result['crack_times_display'].items():
        tk.Label(time_frame, text=f"{attack_type}: {time_str}", padx=18, pady=5, bg="white", fg="black").pack(anchor='w')

    feedback = result.get('feedback', {})
    suggestions = feedback.get('suggestions', [])
    warning = feedback.get('warning', '')

    if warning:
        tk.Label(suggestion_frame, text=f"Warning: {warning}", padx=18, pady=5, bg="white", fg="red", font=("Arial", 10, "italic")).pack(anchor='w')

    if suggestions:
        tk.Label(suggestion_frame, text="Suggestions:", padx=18, pady=5, bg="white", font=("Arial", 12, "bold")).pack(anchor='w')
        for suggestion in suggestions:
            tk.Label(suggestion_frame, text=suggestion, padx=18, pady=5, bg="white", fg="black").pack(anchor='w')

    tk.Button(strength_window, text="Project Info", font=("Arial", 14, "bold"), bg="red", fg="white", command=project_info).pack(pady=20)

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def on_generate():
    length = int(length_var.get())
    generated = generate_password(length)
    generated_var.set(generated)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(generated_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

passwords_list = ["sunflower123", "Monkey!2025", "P@ssw0rd_Example"]
passwords_string = "\n".join(passwords_list)

def copy_dataset_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(passwords_string)
    messagebox.showinfo("Copied", "Passwords list copied to clipboard!")

def open_breach_site(site_url):
    webbrowser.open(site_url)

# ---------- SCROLLABLE MAIN WINDOW SETUP -----------
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("520x900")
root.configure(bg="black")


canvas = tk.Canvas(root, bg="black", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas, bg="black")
canvas.create_window((0, 0), window=frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
frame.bind("<Configure>", on_frame_configure)
def _on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# --------- Put all widgets in frame instead of root ---------
tk.Button(frame, text="Project Info", font=("Arial", 10, "bold"), bg="red", fg="white", command=project_info).pack(pady=10)
tk.Label(frame, text="Password Strength Checker", font=("Arial", 14, "bold"), bg="black", fg="white").pack(pady=5)

try:
    lock_image = Image.open("lock.png")
    lock_image = lock_image.resize((100, 100), Image.Resampling.LANCZOS)
    lock_photo = ImageTk.PhotoImage(lock_image)
    tk.Label(frame, image=lock_photo, bg="black").pack(pady=5)
except Exception as e:
    print(f"Error loading image: {e}")

# ------------- PASSWORD ENTRY + COPY BUTTON -------------
tk.Label(frame, text="Enter Password:", font=("Arial", 12), bg="black", fg="white").pack(pady=10)
password_var = tk.StringVar()
pw_entry_frame = tk.Frame(frame, bg="black")
pw_entry_frame.pack(pady=5)
pw_entry = tk.Entry(pw_entry_frame, textvariable=password_var, show="*", font=("Arial", 12), width=25, justify='center')
pw_entry.pack(side="left")

def copy_password_entry():
    value = password_var.get()
    if value:
        root.clipboard_clear()
        root.clipboard_append(value)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

tk.Button(
    pw_entry_frame,
    text="Copy",
    font=("Arial", 10),
    bg="blue",
    fg="white",
    command=copy_password_entry
).pack(side="left", padx=3)

tk.Button(
    frame,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=20,
    command=lambda: check_password_strength(password_var.get()) if password_var.get() else messagebox.showwarning("Input Error", "Please enter a password!"),
).pack(pady=20)

# ------- Password Generator Section -------
tk.Label(frame, text="Generate Strong Password", font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=10)
length_var = tk.StringVar(value="16")
length_menu = tk.OptionMenu(frame, length_var, "16", "24", "32")
length_menu.config(font=("Arial", 10), bg="white")
length_menu.pack()
tk.Button(frame, text="Generate Password", font=("Arial", 12), bg="green", fg="white", command=on_generate).pack(pady=10)
generated_var = tk.StringVar()
tk.Entry(frame, textvariable=generated_var, font=("Arial", 12), width=30, justify='center').pack(pady=5)
tk.Button(frame, text="Copy to Clipboard", font=("Arial", 10), bg="blue", fg="white", command=copy_to_clipboard).pack(pady=5)

# ------- Leak-Lookup Email/Username section -------
tk.Label(frame, text="Check Breach (Leak-Lookup.com)", font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=10)
email_var = tk.StringVar()
tk.Entry(frame, textvariable=email_var, font=("Arial", 12), width=30, justify='center').pack(pady=5)
tk.Button(frame, text="Check Leak", font=("Arial", 11), bg="purple", fg="white", command=on_lookup).pack(pady=5)

# ------- Dataset Section -------
tk.Label(frame, text="Dataset For Password Analysis", font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=15)
dataset_text = tk.Text(frame, height=5, width=35, font=("Arial", 11), wrap='none')
dataset_text.insert('1.0', passwords_string)
dataset_text.config(state='disabled')
dataset_text.pack()
tk.Button(frame, text="Copy Passwords List (3,4,5)", font=("Arial", 10), bg="orange", fg="black", command=copy_dataset_to_clipboard).pack(pady=6)

# ------- External breach check websites -------
tk.Label(frame, text="Other Breach Check Tools", font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=10)
breach_sites = {
    "Have I Been Pwned": "http://haveibeenpwned.com",
    "BreachDirectory": "http://breachdirectory.org",
    "LeakPeek": "http://leakpeek.com",
    "Leak-Lookup": "http://leak-lookup.com",
    "LostMyPass": "https://www.lostmypass.com/",
    "DeHashed": "https://dehashed.com"
}
for name, url in breach_sites.items():
    tk.Button(frame, text=f"Open {name}", font=("Arial", 10), bg="grey", fg="white", width=30,
              command=lambda u=url: open_breach_site(u)).pack(pady=2)

root.mainloop()
