from docx import Document
from parser import parse_resume

class Editor:

    def __init__(self, file, newer_values):
        self.file_path = file  # store path
        self.document = Document(file)  # let python-docx open it

        self.older_values = parse_resume(file)
        self.improved_general_details = newer_values[0]
        self.improved_experience_details = newer_values[1]

        # Replace professional summary
        old_summary = self.older_values[0]["professional_summary"]
        new_summary = newer_values[0]["professional_summary"]


    def replace_professional_summary(self, old_summary, new_summary):
        # Replace in paragraphs
        for paragraph in self.document.paragraphs:
            if old_summary in paragraph.text:
                for run in paragraph.runs:
                    if old_summary in run.text:
                        run.text = run.text.replace(old_summary, new_summary)

        # Save back to file
        self.document.save(self.file_path)
        print("Updated summary section")

    def replace_experience_details(self, general_details, experience_details):
        pass

