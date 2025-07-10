from plyer import filechooser


path = filechooser.open_file()
print(f"Selected File: {path}")

multple = filechooser.open_file(multiple=True)
print(f"Selected file: {multple}")


save = filechooser.save_file()
print(f"Save the file {save}")
