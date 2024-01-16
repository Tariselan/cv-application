# CV Application

The CV Application is a Tkinter-based tool for creating Curriculum Vitae (CV) documents. It offers a simple interface to input personal information, education details, skills, work experience, and generates a PDF using ReportLab.

## Features

- Input personal details
- Add education, skills, work experience, and other information
- Generate a PDF CV

## Installation
 
1. **Clone the repository:**
   ```bash
   git clone https://github.com/tariselan/cv-application.git
   ```

2.  **Install dependencies**
   ```bash
   pip install tkinter
   pip install reportlab
   pip install ttkthemes
   pip install PyMuPDF
   ```
3. **Run the application**
   ```bash
   python cv.py
   ```

## Usage
1. Launch the application
2. Fill in the details for each section
3. Click "Generate PDF" to create a PDF

## Code Structure
+ **CVSection:** Base class for CV sections
+ **PersonalInformationSection:** Subclass for personal information
+ **EducationSection, SkillsSection, WorkExperienceSection, OtherInformationSection:** Sections for education, skills, work experience, and other information.
+ **CVApp:** Main application class

## License

This project is licensed under the [MIT License](LICENSE).
