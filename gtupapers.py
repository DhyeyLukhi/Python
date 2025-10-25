import webbrowser

year = ['W2024', 'W2023', 'W2022', 'W2021']
code = [3150005, 3151606, 3150710, 3150709, 3151608, 3150703]

for c in code:
    for y in year:
        url = f"https://gtu.ac.in/uploads/{y}/BE/{c}.pdf"
        webbrowser.open(url)