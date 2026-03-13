from pathlib import Path


p = Path("hej.txt")
print(p.absolute())
p.touch()

p_d = Path("Subfolder")
p_d.mkdir(exist_ok=True)

new_path = p_d / p
print(new_path.absolute())
new_path.touch()