from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

# Define the list of Git commands
git_commands = [
    "git init - Initialize a new Git repository",
    "git clone - Clone a remote repository to your local machine",
    "git add - Add files to the staging area",
    "git commit - Commit changes to the local repository",
    "git push - Push commits from the local repository to a remote repository",
    "git pull - Pull changes from a remote repository to your local repository",
    "git status - Show the status of files in the working directory and staging area",
    "git branch - List, create, or delete branches",
    "git checkout - Switch between branches or restore files",
    "git merge - Merge changes from one branch into another",
    "git log - Show the commit history",
    "git diff - Show changes between commits, branches, or files",
    "git reset - Undo commits or unstage files",
    "git stash - Temporarily save changes for later use",
    "git remote - Manage remote repository connections"
]

# Create a PDF document
doc = SimpleDocTemplate("git_commands.pdf", pagesize=letter)
elements = []

# Create styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'Title',
    parent=styles['Heading1'],
    alignment=TA_CENTER,
    fontSize=24,
    textColor=HexColor('#333333')
)
command_style = ParagraphStyle(
    'Command',
    parent=styles['BodyText'],
    fontSize=14,
    textColor=HexColor('#555555'),
    leftIndent=30
)

# Add the Git logo
logo = Image('git-logo.jpg', width=2*inch, height=2*inch)
elements.append(logo)
elements.append(Spacer(1, 24))  # Add some space after the logo

# Add the title
title = Paragraph("Important Git Commands", title_style)
elements.append(title)
elements.append(Spacer(1, 18))  # Add some space after the title

# Add a horizontal rule
elements.append(Image('horizontal.jpg', width=6*inch, height=0.1*inch))
elements.append(Spacer(1, 12))  # Add some space after the rule

# Add each Git command as a paragraph to the PDF
for command in git_commands:
    paragraph = Paragraph(command, command_style)
    elements.append(paragraph)
    elements.append(Spacer(1, 8))  # Add some space between commands

# Build the PDF document
doc.build(elements)