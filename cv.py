import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4 
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageTemplate, Spacer

from ttkthemes import ThemedStyle

class CVSection:
    def __init__(self, root, style_heading, title):
        self.root = root
        self.style_heading = style_heading
        self.title = title
        self.widgets = {}
        self.create_widgets()

    def create_widgets(self):
        self.widgets["frame"] = ttk.Frame(self.root, padding=(20, 10))
        self.widgets["frame"].grid(row=0, column=0, columnspan=2, sticky="ew")
        raise NotImplementedError("Subclasses must implement the 'create_widgets' method.")

    def validate_input(self):
        raise NotImplementedError("Subclasses must implement the 'validate_input' method.")

    def get_data(self):
        raise NotImplementedError("Subclasses must implement the 'get_data' method.")

class PersonalInformationSection(CVSection):
    DEFAULT_VALUES = {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "john.doe@example.com",
        "address": "123 Main Street, City, Country",
        "statement": "Results-oriented professional with..."
    }

    def create_widgets(self):
        self.widgets["frame"] = ttk.Frame(self.root, padding=(10, 5))
        self.widgets["frame"].grid(row=0, column=0, columnspan=2, sticky="ew")

        labels_entries = [
            ("Full Name:", "name"), ("Phone Number:", "phone"), ("Email Address:", "email"),
            ("Residential Address:", "address"), ("Personal Statement:", "statement")
        ]

        for row, (label_text, entry_key) in enumerate(labels_entries, start=1):
            label = ttk.Label(self.widgets["frame"], text=label_text)
            entry = ttk.Entry(self.widgets["frame"])
            label.grid(row=row, column=0, sticky="E", padx=5, pady=5)
            entry.grid(row=row, column=1, sticky="W", padx=5, pady=5)
            self.widgets[entry_key + "_entry"] = entry

            # Set default values
            default_value = self.DEFAULT_VALUES.get(entry_key, "")
            entry.insert(0, default_value)

    def validate_input(self):
        required_fields = {
            "Full Name": self.widgets["name_entry"].get(),
            "Phone Number": self.widgets["phone_entry"].get(),
            "Email Address": self.widgets["email_entry"].get()
        }

        for field, value in required_fields.items():
            if not value:
                messagebox.showerror("Error", f"{field} is required.")
                return False

        return True

    def get_data(self):
        return {
            "full_name": self.widgets["name_entry"].get(),
            "phone_number": self.widgets["phone_entry"].get(),
            "email_address": self.widgets["email_entry"].get(),
            "residential_address": self.widgets["address_entry"].get(),
            "personal_statement": self.widgets["statement_entry"].get(),
        }

class EducationSection(CVSection):
    DEFAULT_VALUES = {
        "school": "High School XYZ",
        "graduation": "June 2023"
    }

    def create_widgets(self):
        self.widgets["frame"] = ttk.Frame(self.root, padding=(10, 5))
        self.widgets["frame"].grid(row=1, column=0, columnspan=2, sticky="ew")

        self.widgets["education_label"] = ttk.Label(self.widgets["frame"], text=self.title, font=('Helvetica', 16, 'bold'))
        self.widgets["education_label"].grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        labels_entries = [("High School:", "school"), ("Expected Graduation Date:", "graduation")]

        for row, (label_text, entry_key) in enumerate(labels_entries, start=1):
            label = ttk.Label(self.widgets["frame"], text=label_text)
            entry = ttk.Entry(self.widgets["frame"])
            label.grid(row=row, column=0, sticky="E", padx=5, pady=5)
            entry.grid(row=row, column=1, sticky="W", padx=5, pady=5)
            self.widgets[entry_key + "_entry"] = entry

            # Set default values
            default_value = self.DEFAULT_VALUES.get(entry_key, "")
            entry.insert(0, default_value)

    def validate_input(self):
        # Additional validation can be added if needed
        return True

    def get_data(self):
        return {
            "high_school": self.widgets["school_entry"].get(),
            "graduation_date": self.widgets["graduation_entry"].get()
        }

class SkillsSection(CVSection):
    def create_widgets(self):
        self.widgets["frame"] = ttk.Frame(self.root, padding=(10, 5))
        self.widgets["frame"].grid(row=2, column=0, columnspan=2, sticky="ew")

        self.widgets["skills_label"] = ttk.Label(self.widgets["frame"], text=self.title, font=('Helvetica', 16, 'bold'))
        self.widgets["skills_label"].grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        self.widgets["skills_entry"] = tk.Text(self.widgets["frame"], height=4, width=40)
        self.widgets["skills_entry"].grid(row=1, column=0, columnspan=2, sticky="n", pady=5)

    def validate_input(self):
        # Additional validation can be added if needed
        return True

    def get_data(self):
        return {
            "skills": self.widgets["skills_entry"].get("1.0", tk.END).strip()
        }

class WorkExperienceSection(CVSection):
    def create_widgets(self):
        self.widgets["frame"] = ttk.Frame(self.root, padding=(10, 5))
        self.widgets["frame"].grid(row=3, column=0, columnspan=2, sticky="ew")

        self.widgets["work_label"] = ttk.Label(self.widgets["frame"], text=self.title, font=('Helvetica', 16, 'bold'))
        self.widgets["work_label"].grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        self.widgets["experience_entry"] = tk.Text(self.widgets["frame"], height=4, width=40)
        self.widgets["experience_entry"].grid(row=1, column=0, columnspan=2, sticky="n", pady=5)

    def validate_input(self):
        # Additional validation can be added if needed
        return True

    def get_data(self):
        return {
            "work_experience": self.widgets["experience_entry"].get("1.0", tk.END).strip()
        }

class OtherInformationSection(CVSection):
    def create_widgets(self):
        self.widgets["frame"] = ttk.Frame(self.root, padding=(10, 5))
        self.widgets["frame"].grid(row=4, column=0, columnspan=2, sticky="ew")

        self.widgets["other_label"] = ttk.Label(self.widgets["frame"], text=self.title, font=('Helvetica', 16, 'bold'))
        self.widgets["other_label"].grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        labels_entries = [
            ("Achievements and Awards:", "achievements"),
            ("Extracurricular Activities:", "activities"),
            ("References:", "references")
        ]

        for row, (label_text, entry_key) in enumerate(labels_entries, start=1):
            label = ttk.Label(self.widgets["frame"], text=label_text)
            entry = ttk.Entry(self.widgets["frame"])
            label.grid(row=row, column=0, sticky="E", padx=5, pady=5)
            entry.grid(row=row, column=1, sticky="W", padx=5, pady=5)
            self.widgets[entry_key + "_entry"] = entry

    def validate_input(self):
        # Additional validation can be added if needed
        return True

    def get_data(self):
        return {
            "achievements": self.widgets["achievements_entry"].get(),
            "activities": self.widgets["activities_entry"].get(),
            "references": self.widgets["references_entry"].get()
        }

class TopImagePageTemplate(SimpleDocTemplate):
    def __init__(self, filename, **kwargs):
        SimpleDocTemplate.__init__(self, filename, pagesize=A4, **kwargs)
        self.topImage = None
        self.topImageHeight = 0

    def build(self, flowables, filename=None, canvasmaker=None):
        self.topImage = utils.ImageReader(self.topImage)  # Load the image
        super().build(flowables, filename=filename, canvasmaker=canvasmaker)

    def afterFlowable(self, flowable, canvas, doc):
        if isinstance(flowable, Paragraph) and self.topImage:
            # Calculate the height needed for the image
            _, line_height = flowable.wrap(doc.width, doc.height)
            self.topImageHeight = line_height

    def getPageTemplate(self, page_number):
        return PageTemplate('topImage', pagesize=A4)

class PDFGenerator:
    @staticmethod
    def add_section_to_pdf(pdf_doc, section, data):
        content = []

        # Add a section header
        content.append(Paragraph(section.title, section.style_heading))

        # Add section content
        section_data = section.get_data()
        for label, value in section_data.items():
            content.append(Paragraph(f"{label}: {value}", section.style_heading))

        content.append(Spacer(1, 12))
        pdf_doc.build(content)

    @staticmethod
    def generate_content(style_heading, sections):
        pdf_filename = "generated_cv.pdf"
        pdf_doc = SimpleDocTemplate(pdf_filename, pagesize=A4)

        for section in sections:
            PDFGenerator.add_section_to_pdf(pdf_doc, section, section.get_data())

        return pdf_filename
    
class CVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CV App")
        self.root.geometry("650x750")
        self.root.resizable(False, False)

        self.style = ThemedStyle(self.root)
        self.style.set_theme("plastik")

        self.styles = getSampleStyleSheet()
        self.style_heading = self.styles['Heading1']

        self.sections = [
            PersonalInformationSection(self.root, self.style_heading, "Personal Information"),
            EducationSection(self.root, self.style_heading, "Education"),
            SkillsSection(self.root, self.style_heading, "Skills"),
            WorkExperienceSection(self.root, self.style_heading, "Work Experience"),
            OtherInformationSection(self.root, self.style_heading, "Other Information")
        ]

        self.center_and_configure()
        self.create_widgets()

        self.submit_button = ttk.Button(self.root, text="Generate CV", command=self.generate_pdf)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=3, sticky="n")

        self.generate_pdf_button = ttk.Button(self.root, text="Generate PDF", command=self.generate_pdf)
        self.generate_pdf_button.grid(row=5, column=0, columnspan=2, pady=3, sticky="n")

    def generate_pdf(self):
        if not self.validate_input():
            return

        data = {}
        for section in self.sections:
            data.update(section.get_data())

        pdf_filename = PDFGenerator.generate_content(self.style_heading, self.sections)
        print(f"PDF generated: {pdf_filename}")

    def center_and_configure(self):
        self.root.eval('tk::PlaceWindow . center')

        for i in range(2):
            self.root.columnconfigure(i, weight=1)
        for i in range(5):
            self.root.rowconfigure(i, weight=1)

    def create_widgets(self):
        for section in self.sections:
            section.widgets["frame"].columnconfigure(0, weight=1)
            section.widgets["frame"].columnconfigure(1, weight=1)

    def validate_input(self):
        return all(section.validate_input() for section in self.sections)


if __name__ == "__main__":
    root = tk.Tk()
    app = CVApp(root)
    root.mainloop()
