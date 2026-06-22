import webbrowser

year = ['S2025', 'S2024', 'S2023', 'S2022', 'W2025', 'W2024', 'W2023', 'W2022']
code = [3161605]

for c in code:
    for y in year:
        url = f"https://gtu.ac.in/uploads/{y}/BE/{c}.pdf"
        webbrowser.open(url)