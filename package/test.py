# import os
# import pkg_resources
# from rich.progress import Progress


# def get_package_sizes():
#     package_sizes = {}
#     for dist in pkg_resources.working_set:
#         package_sizes[dist.project_name] = dist.location
#     return package_sizes

# def calculate_sizes(package_sizes):
#     total_size = 0
#     with Progress() as progress:
#         task = progress.add_task("Calculating sizes...", total=len(package_sizes))
#         for package, path in package_sizes.items():
#             size = sum(os.path.getsize(os.path.join(path, f)) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)))
#             total_size += size
#             print(f"\r{package}: {size / (1024 * 1024):.2f} MB", end="", flush=True)
#             progress.update(task, advance=1)
#         print(f"Total Size: {total_size / (1024 * 1024):.2f} MB")

# if __name__ == "__main__":
#     package_sizes = get_package_sizes()
#     calculate_sizes(package_sizes)

# import os

# def getWorker() -> str:
#     path = os.getcwd()

#     if "/" in path:
#         return path.split("/")[-1]
#     elif "\\" in path:
#         return path.split("\\")[-1]
#     else:return path

# print(getWorker())

import ast

def get_imported_modules(file_path):
    with open(file_path, 'r') as file:
        node = ast.parse(file.read(), filename=file_path)
    
    imports = set()
    for elem in ast.walk(node):
        if isinstance(elem, ast.Import):
            for alias in elem.names:
                imports.add(alias.name)
        elif isinstance(elem, ast.ImportFrom):
            imports.add(elem.module)
    
    return imports

# Example usage
file_path = 'package/ffp.py'
print(get_imported_modules(file_path))
