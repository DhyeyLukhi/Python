import subprocess
import webbrowser

def define(word):
    result = subprocess.run(["dict", word], capture_output=True, text=True)
    if result.returncode == 0:
        
        print(result.stdout)
        print(f"https://www.google.com/search?q={word}")
    else:
        url = f"https://www.google.com/search?q={word}"
        webbrowser.open(url)

define(input("Word: "))