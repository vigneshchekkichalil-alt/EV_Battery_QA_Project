import os

folders = [
    "src",
    "tests",
    "docs",
    "reports",
    "automation"
]

files = [
    "README.md"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

for file in files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            pass
        print(f"Created file: {file}")

print("\nProject structure created successfully.")