import periodictable as pt

number = int(input("Enter Element No: "))

element = pt.elements[number]
print(f"Atomic Symbol: {element.symbol}")
print(f"Atomic name: {element.name}")
print(f"Atomic mass: {element.mass}")
print(f"Atomic density: {element.density} {element.density_units}")
print(f"Charge: {element.charge}")
print(f"Ion: {element.ion.element_or_isotope}")
print(f"Ions: {element.ions}")
print(f"iostopes: {element.isotopes}")
print(pt.mix_by_volume())
