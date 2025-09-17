# Movies Recommendation System

This project is a movie recommendation system that utilizes a Jupyter notebook for data processing and model training, and a Streamlit application for the web interface.

## Project Structure

- **Movies_Recommendar.ipynb**: Contains the Jupyter notebook with data processing, model training, and recommendation logic.
- **app.py**: The main application script that creates a web interface for the movie recommendation system using Streamlit.
- **requirements.txt**: Lists the dependencies required to run the project.
- **README.md**: Documentation for the project.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Movies_Recommendar
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command:
```
streamlit run app.py
```

This will start the application, and you can access it in your web browser at `http://localhost:8501`.

## Usage

1. Select a movie from the dropdown menu.
2. Click on "Show Recommendation" to get a list of recommended movies based on the selected movie.

## Acknowledgments

- This project uses the TMDB API for movie data.