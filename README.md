Cybercrime Report Analysis


This project is developed for the IndiaAI CyberGuard AI Hackathon, where the goal is to analyze cybercrime reports using a Natural Language Processing (NLP) model. The application provides an interface for users to input a cybercrime report (via text or file upload), which is then processed and analyzed to generate insights.

Project Overview
This application leverages NLP to understand and analyze the content of cybercrime reports. Users can input a report directly or upload a file, and the system will provide a summary or classification of the report based on the implemented NLP model.

Key Features
Text and File Upload: Users can either type in a report or upload a file (in .txt, .pdf, .doc, or .docx formats).
Real-time Analysis: The application provides an "Analyze Report" button to process the input and display the analysis results in real-time.
User-friendly Interface: Built with a clean and responsive UI using Tailwind CSS, making it accessible across devices.


Tech Stack
Backend: Flask (Python) for handling requests and performing the analysis.
Frontend: HTML, JavaScript, and Tailwind CSS for responsive styling.
Machine Learning/NLP: Natural Language Processing techniques (models and tools) to analyze and classify the input reports.


Getting Started
Prerequisites
Python 3.x installed on your system.
Virtual Environment (recommended) to manage dependencies.
Installation

Clone the repository:

bash
Copy code
git clone https://github.com/sunitachoudhary0280/cybercrimereport.git
cd cybercrime-report-analysis
Set up the virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Application
Start the Flask server:

bash
Copy code
python app.py
Open a web browser and go to http://localhost:5000 to access the application.



Usage

Enter your cybercrime report in the text box or upload a report file.
Click on the "Analyze Report" button.
The system will analyze the report, and the results will be displayed on the screen.

Project Structure
app.py: The Flask backend script that handles requests and performs NLP analysis.
index.html: The frontend file with HTML and JavaScript for the user interface.
requirements.txt: Lists the necessary dependencies to run the application.

Future Enhancements
Advanced NLP Models: Integrate more sophisticated models for deeper analysis.
Additional File Types: Support for more file types and formats.
Detailed Classification: Provide a more detailed analysis report with visualizations.

License
This project is licensed under the MIT License.

Contact
For any questions, feel free to reach out to the project developer or open an issue on the repository.
