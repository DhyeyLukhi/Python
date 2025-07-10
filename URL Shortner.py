import pyshorteners


url = input("URL: ")
type_tiny = pyshorteners.Shortener()

short_url = type_tiny.tinyurl.short(url)

print(f"New URL: {short_url}")

