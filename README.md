# TalentMate

TalentMate is a Generative AI-powered Hiring Assistant designed to streamline the interview process by generating theoretical interview questions, collecting candidate responses, and providing recruiters with easy access to candidate evaluations.

## Features

- **Candidate Registration:** Users can register by providing their details.
- **AI-Generated Interview Questions:** Questions are generated dynamically based on the selected technology stack.
- **Interview Process:** Candidates answer AI-generated questions in an interview form.
- **Response Storage:** Candidate responses are stored in a database.
- **Recruiter Dashboard:** Recruiters can view candidate details and responses.

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** SQLite
- **AI Integration:** Hugging Face models
- **Other Libraries:** dotenv (for API keys), re (for text processing), SQLite3 (for database management)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Abhisek8895/TalentMate.git
   cd TalentMate
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file and add your Hugging Face API key:
   ```
   HUGGINGFACE_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```sh
   streamlit run app.py
   ```

## Database Structure

The project uses an SQLite database with the following tables:

### `candidates` Table
| Column       | Type    | Description              |
|-------------|--------|--------------------------|
| id          | INT    | Primary Key (Auto Increment) |
| name        | TEXT   | Candidate's name        |
| email       | TEXT   | Candidate's email       |
| phone       | TEXT   | Contact number          |
| experience  | INT    | total experience        |
| position    | TEXT   | Desired Position        |
| location    | TEXT   | Current location        |
| tech_stack  | TEXT   | Technology expertise    |

### `responses` Table
| Column       | Type    | Description                |
|-------------|--------|----------------------------|
| id          | INT    | Primary Key (Auto Increment) |
| candidate_id| INT    | Foreign Key (candidates.id) |
| question    | TEXT   | Interview question         |
| answer      | TEXT   | Candidate's response      |

## Usage Guide

1. **Register a Candidate:** The candidate submits their details and selects their technology stack.
2. **Interview Process:** AI generates theoretical questions, and candidates submit their answers.
3. **Recruiter Review:** The recruiter can access candidate responses via the dashboard.

## Future Enhancements
- **Resume Upload Feature**
- **Recruiter Evaluation System**
- **Automated Scoring for Candidate Responses**

## License
This project is open-source and free to use.

---

🚀 **TalentMate** is an AI-powered hiring assistant that simplifies the recruitment process for both candidates and recruiters. Happy hiring!

