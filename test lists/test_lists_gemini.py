from docx import Document
from docx.enum.style import WD_STYLE_TYPE  # Import for newer versions

def create_numbered_lists(doc, content, restart_points):
  """
  Creates multiple numbered lists with restarts in a document

  Args:
      doc: The docx.Document object
      content: List of lists, where each sublist represents a numbered list section
      restart_points: List of indexes within 'content' where numbering should restart
  """
  default_style = doc.styles["List Number"]
  abstract_num = default_style.paragraph_format.list_definition.abstract_num

  for i, items in enumerate(content):
    for item in items:
      paragraph = doc.add_paragraph(item)
      paragraph.style = default_style

      # Check for restart point and create new numbering definition if needed
      if i in restart_points:
        new_num = abstract_num.clone()
        new_num.restart_level = WD_STYLE_TYPE.LIST  # Adjust for older versions (see note below)
        new_style = doc.styles.add_style("List Number - Restart", WD_STYLE_TYPE.LIST)
        new_style.base_style = default_style
        new_style.paragraph_format.list_definition = new_num
        paragraph.style = new_style

# Example usage with compatibility note
document = Document()
content = [
  ["Item 1", "Item 2", "Item 3"],
  ["Item 4", "Item 5"],
  ["Item 6", "Item 7", "Item 8"],
]
restart_points = [1, 2]

# For older versions of python-docx (without docx.enum.list):
# Replace the line with:
# new_num.restart_level = list_types.WD_LIST_TYPE.NUMBER

create_numbered_lists(document, content, restart_points)

document.save("multiple_numbered_lists.docx")