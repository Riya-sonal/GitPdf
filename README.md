
```markdown
# Git Commands PDF Generator

This Python project allows you to generate a stylish PDF document containing a list of important Git commands. The PDF features a modern design, a custom font, and visually appealing elements like a decorative line separator.

## Features

- Generate a PDF file with a list of essential Git commands
- Customizable title and command styles
- Inclusion of the Git logo
- Decorative line separator for visual appeal
- Adjustable spacing and layout for improved readability

## Prerequisites

- Python 3.x
- `reportlab` library

## Installation

1. Clone the repository:

```
git clone https://github.com/Riya-sonal/GitPdf.git
```

2. Install the required dependencies:

```
pip install reportlab
```

3. Ensure you have the following files in the project directory:
   - `git-logo.png` (Git logo image)
   - `horizontal-line.png` (Decorative line image)

## Usage

1. Open the `git.py` file in a text editor.
2. Customize the styles, colors, or any other settings according to your preferences.
3. Run the script:

```
python git.py
```

4. The script will generate a PDF file named `git_commands.pdf` in the same directory.

## Customization

You can further customize the PDF by modifying the following aspects in the `git.py` script:

- Title and command styles (font, size, color, alignment, etc.)
- Spacing and layout adjustments
- Color scheme
- Decorative elements (lines, shapes, etc.)
- Custom font (replace the Montserrat font with your desired font)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- The `reportlab` library for enabling PDF generation in Python.
```
