import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
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


class PDFGenerator:
    @staticmethod
    def generate_content(style_heading, **data):
        content = []

        # Add a professional header
        header_text = f"{data['full_name']}"
        content.append(Paragraph(header_text, style_heading))

        # Personal Information
        content.append(Paragraph("Contact Information", style_heading))
        contact_table_data = [
            ['Phone Number:', data['phone_number']],
            ['Email Address:', data['email_address']],
            ['Residential Address:', data['residential_address']],
            ['Personal Statement:', data['personal_statement']]
        ]
        contact_table = Table(contact_table_data, colWidths=[150, 400])
        content.append(contact_table)
        content.append(Spacer(1, 12))

        # Education and Experience
        content.append(Paragraph("Education and Experience", style_heading))
        education_table_data = [
            ['High School:', data['high_school']],
            ['Expected Graduation Date:', data['graduation_date']],
            ['Skills:', data['skills']],
            ['Work Experience:', data['work_experience']]
        ]
        education_table = Table(education_table_data, colWidths=[150, 400])
        content.append(education_table)
        content.append(Spacer(1, 12))

        # Achievements and References
        content.append(Paragraph("Achievements and References", style_heading))
        achievements_table_data = [
            ['Achievements and Awards:', data['achievements']],
            ['Extracurricular Activities:', data['activities']],
            ['References:', data['references']]
        ]
        achievements_table = Table(achievements_table_data, colWidths=[150, 400])
        content.append(achievements_table)

        return content


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

        self.submit_button = ttk.Button(self.root, text="Generate CV", command=self.generate_cv)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=3, sticky="n")

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

    def generate_cv(self):
        if not self.validate_input():
            return

        data = {}
        for section in self.sections:
            data.update(section.get_data())

        pdf_filename = "generated_cv.pdf"
        content = PDFGenerator.generate_content(self.style_heading, **data)
        self.create_pdf(pdf_filename, content)

    def create_pdf(self, pdf_filename, content):
        pdf_doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        pdf_doc.build(content)


if __name__ == "__main__":
    root = tk.Tk()
    app = CVApp(root)
    root.mainloop()
