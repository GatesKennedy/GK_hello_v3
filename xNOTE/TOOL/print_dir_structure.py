import os
import sys
from pathlib import Path
from datetime import datetime

# Common patterns to ignore in Python projects
IGNORE_PATTERNS = {
	# Version Control
	".git",

	# Python
	"__pycache__",
	".pytest_cache",
	"*.pyc",
	"*.pyo",
	"*.pyd",
	".Python",
	"env",
	"venv",
	".env",
	".venv",
	"ENV",

	# IDE/Editor
	".vscode",
	".idea",
	"*.swp",
	"*.swo",
	".vs",

	# Build/Distribution
	"build",
	"develop-eggs",
	"dist",
	"downloads",
	"eggs",
	"lib",
	"lib64",
	"parts",
	"sdist",
	"var",
	"wheels",
	"*.egg-info",
	"*.egg",

	# Coverage/Linting
	".coverage",
	".tox",
	".nox",
	"htmlcov",
	".mypy_cache",
	".ruff_cache",
	".pylint.d"
}

def should_include(path: Path) -> bool:
	"""
	Determine if a path should be included in the tree.

	Args:
		path: Path object to check

	Returns:
		Boolean indicating if path should be included
	"""
	# Check if path matches any ignore pattern
	for pattern in IGNORE_PATTERNS:
		# Handle glob patterns
		if pattern.startswith("*"):
			if path.name.endswith(pattern[1:]):
				return False
		# Handle directory/file names
		elif pattern in path.parts or path.name == pattern:
			return False
	return True

def generate_tree_content(directory_path: str, prefix: str = "", is_last: bool = True) -> list:
	"""
	Generate directory tree structure content as a list of strings.

	Args:
		directory_path: The path to start traversing from
		prefix: Current line prefix for formatting
		is_last: Boolean indicating if current item is last in its group

	Returns:
		List of strings containing the tree structure
	"""
	directory = Path(directory_path)

	# Skip ignored paths
	if not should_include(directory):
		return []

	content = []

	# Format current directory/file line
	if is_last:
		content.append(f"{prefix}└── {directory.name}")
		new_prefix = prefix + "	"
	else:
		content.append(f"{prefix}├── {directory.name}")
		new_prefix = prefix + "│	"

	# Process directory contents
	if directory.is_dir():
		items = list(directory.iterdir())
		# Filter out ignored paths
		items = [item for item in items if should_include(item)]
		items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

		for index, item in enumerate(items):
			is_last_item = index == len(items) - 1
			content.extend(generate_tree_content(str(item), new_prefix, is_last_item))

	return content

def write_tree_to_markdown(root_path: str, output_file: str = "directory_structure.md") -> None:
	"""
	Write the directory tree structure to a markdown file.

	Args:
		root_path: The root directory path to start from
		output_file: The name of the output markdown file
	"""
	# Verify path exists
	if not os.path.exists(root_path):
		print(f"Error: Path '{root_path}' does not exist")
		sys.exit(1)

	# Generate content
	content = ["# Python Project Directory Structure\n"]
	content.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
	content.append(f"Root path: {os.path.abspath(root_path)}\n")
	content.append("Note: Common Python development folders and files are ignored\n")
	content.append("```")
	content.extend(generate_tree_content(root_path))
	content.append("```")

	# Write to file
	try:
		with open(output_file, 'w', encoding='utf-8') as f:
			f.write('\n'.join(content))
		print(f"Directory structure has been written to {output_file}")
	except Exception as e:
		print(f"Error writing to file: {e}")
		sys.exit(1)

def main():
	# Get path from command line argument or use current directory
	if len(sys.argv) > 1:
		root_path = sys.argv[1]
	else:
		root_path = "."

	# Get output filename from second argument or use default
	output_file = sys.argv[2] if len(sys.argv) > 2 else "directory_structure.md"

	# Generate and write tree structure
	write_tree_to_markdown(root_path, output_file)

if __name__ == "__main__":
	main()