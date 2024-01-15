import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table

from ttkthemes import ThemedStyle
from reportlab.lib.styles import getSampleStyleSheet  

class CVSection:
    def __init__(self, root, style_heading, title):
        self.root = root
        self.style_heading = style_heading
        self.title = title
        self.widgets = {}
        self.create_widgets()

    def create_widgets(self):
        # Create a frame with padding
        self.widgets["frame"] = ttk.Frame(self.root, padding=(20, 10))
        self.widgets["frame"].grid(row=0, column=0, columnspan=2, sticky="ew")
        raise NotImplementedError("Subclasses must implement the 'create_widgets' method.")
        

    def validate_input(self):
        raise NotImplementedError("Subclasses must implement the 'validate_input' method.")

    def get_data(self):
        raise NotImplementedError("Subclasses must implement the 'get_data' method.")

class PersonalInformationSection(CVSection):
    def create_widgets(self):
        self.widgets["frame"] = ttk.Frame(self.root, padding=(10, 5))
        self.widgets["frame"].grid(row=0, column=0, columnspan=2, sticky="ew")

        self.widgets["name_label"] = ttk.Label(self.widgets["frame"], text="Full Name:")
        self.widgets["name_entry"] = ttk.Entry(self.widgets["frame"])

        self.widgets["phone_label"] = ttk.Label(self.widgets["frame"], text="Phone Number:")
        self.widgets["phone_entry"] = ttk.Entry(self.widgets["frame"])

        self.widgets["email_label"] = ttk.Label(self.widgets["frame"], text="Email Address:")
        self.widgets["email_entry"] = ttk.Entry(self.widgets["frame"])

        self.widgets["address_label"] = ttk.Label(self.widgets["frame"], text="Residential Address:")
        self.widgets["address_entry"] = ttk.Entry(self.widgets["frame"])

        self.widgets["statement_label"] = ttk.Label(self.widgets["frame"], text="Personal Statement:")
        self.widgets["statement_entry"] = ttk.Entry(self.widgets["frame"], width=40)

        row = 1
        for label_key, entry_key in [("name", "name"), ("phone", "phone"), ("email", "email"),
                                     ("address", "address"), ("statement", "statement")]:
            self.widgets[label_key+"_label"].grid(row=row, column=0, sticky="E", padx=5, pady=5)
            self.widgets[entry_key+"_entry"].grid(row=row, column=1, sticky="W", padx=5, pady=5)
            row += 1

        # Default values
        default_values = {
            "name": "John Doe",
            "phone": "123-456-7890",
            "email": "john.doe@example.com",
            "address": "123 Main Street, City, Country",
            "statement": "Results-oriented professional with..."
        }

        # Set default values to the Entry widgets
        for key, default_value in default_values.items():
            self.widgets[key + "_entry"].insert(0, default_value)

        row = 1
        for label_key, entry_key in [("name", "name"), ("phone", "phone"), ("email", "email"),
                                     ("address", "address"), ("statement", "statement")]:
            self.widgets[label_key+"_label"].grid(row=row, column=0, sticky="E", padx=5, pady=5)
            self.widgets[entry_key+"_entry"].grid(row=row, column=1, sticky="W", padx=5, pady=5)
            row += 1

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
    def create_widgets(self):
        self.widgets["frame"] = ttk.Frame(self.root, padding=(10, 5))
        self.widgets["frame"].grid(row=1, column=0, columnspan=2, sticky="ew")

        self.widgets["education_label"] = ttk.Label(self.widgets["frame"], text=self.title, font=('Helvetica', 16, 'bold'))
        self.widgets["education_label"].grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        # High School
        self.widgets["school_label"] = ttk.Label(self.widgets["frame"], text="High School:")
        self.widgets["school_entry"] = ttk.Entry(self.widgets["frame"])

        # Graduation Date
        self.widgets["graduation_label"] = ttk.Label(self.widgets["frame"], text="Expected Graduation Date:")
        self.widgets["graduation_entry"] = ttk.Entry(self.widgets["frame"])

        row = 1
        for label_key, entry_key in [("school", "school"), ("graduation", "graduation")]:
            self.widgets[label_key+"_label"].grid(row=row, column=0, sticky="E", padx=5, pady=5)
            self.widgets[entry_key+"_entry"].grid(row=row, column=1, sticky="W", padx=5, pady=5)
            row += 1
        
        # Default values
        default_values = {
            "school": "High School XYZ",
            "graduation": "June 2023"
        }

        # Set default values to the Entry widgets
        for key, default_value in default_values.items():
            self.widgets[key + "_entry"].insert(0, default_value)

        row = 1
        for label_key, entry_key in [("school", "school"), ("graduation", "graduation")]:
            self.widgets[label_key+"_label"].grid(row=row, column=0, sticky="E", padx=5, pady=5)
            self.widgets[entry_key+"_entry"].grid(row=row, column=1, sticky="W", padx=5, pady=5)
            row += 1

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

        # Achievements and Awards
        self.widgets["achievements_label"] = ttk.Label(self.widgets["frame"], text="Achievements and Awards:")
        self.widgets["achievements_entry"] = ttk.Entry(self.widgets["frame"])

        # Extracurricular Activities
        self.widgets["activities_label"] = ttk.Label(self.widgets["frame"], text="Extracurricular Activities:")
        self.widgets["activities_entry"] = ttk.Entry(self.widgets["frame"])

        # References
        self.widgets["references_label"] = ttk.Label(self.widgets["frame"], text="References:")
        self.widgets["references_entry"] = ttk.Entry(self.widgets["frame"])

        row = 1
        for label_key, entry_key in [("achievements", "achievements"), ("activities", "activities"), ("references", "references")]:
            self.widgets[label_key+"_label"].grid(row=row, column=0, sticky="E", padx=5, pady=5)
            self.widgets[entry_key+"_entry"].grid(row=row, column=1, sticky="W", padx=5, pady=5)
            row += 1

    def validate_input(self):
        # Additional validation can be added if needed
        return True

    def get_data(self):
        return {
            "achievements": self.widgets["achievements_entry"].get(),
            "activities": self.widgets["activities_entry"].get(),
            "references": self.widgets["references_entry"].get()
        }

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
        # Center the window
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
        self.create_pdf(pdf_filename, **data)

    def create_pdf(self, pdf_filename, full_name, phone_number, email_address, residential_address,
                   personal_statement, high_school, graduation_date, skills, work_experience,
                   achievements, activities, references):
        pdf_doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        style_body = self.styles['BodyText']
        style_heading2 = self.styles['Heading2']

        content = []

        # Add a professional header
        header_text = f"{full_name}"
        content.append(Paragraph(header_text, self.style_heading))

        # Personal Information
        content.append(Paragraph("Contact Information", style_heading2))
        contact_table_data = [['Phone Number:', phone_number],
                              ['Email Address:', email_address],
                              ['Residential Address:', residential_address],
                              ['Personal Statement:', personal_statement]]
        contact_table = Table(contact_table_data, colWidths=[150, 400])
        content.append(contact_table)
        content.append(Spacer(1, 12))

        # Education and Experience
        content.append(Paragraph("Education and Experience", style_heading2))
        education_table_data = [['High School:', high_school],
                                ['Expected Graduation Date:', graduation_date],
                                ['Skills:', skills],
                                ['Work Experience:', work_experience]]
        education_table = Table(education_table_data, colWidths=[150, 400])
        content.append(education_table)
        content.append(Spacer(1, 12))

        # Achievements and References
        content.append(Paragraph("Achievements and References", style_heading2))
        achievements_table_data = [['Achievements and Awards:', achievements],
                                   ['Extracurricular Activities:', activities],
                                   ['References:', references]]
        achievements_table = Table(achievements_table_data, colWidths=[150, 400])
        content.append(achievements_table)

        pdf_doc.build(content)

if __name__ == "__main__":
    root = tk.Tk()
    app = CVApp(root)
    root.mainloop()