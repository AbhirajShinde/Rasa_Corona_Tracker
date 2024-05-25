# Corona Tracker Assistant

## Description
This project is a Rasa assistant integrated with Flask that provides information and tracking for COVID-19 cases statewise in India. The assistant uses a third-party API to fetch the latest data on corona patients.

## Installation

### Prerequisites
- Python 3.9.10
- Rasa framework
- Flask

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/AbhirajShinde/Rasa_Corona_Tracker.git
    ```
2. Change to the project directory:
    ```sh
    cd Rasa_Corona_Tracker
    ```
3. Create and activate a virtual environment named `rasaenv`:
    ```sh
    python -m venv rasaenv
    source rasaenv/bin/activate  # On Windows use `.\rasaenv\Scripts\activate`
    ```
4. Install the dependencies:
    ```sh
    pip install rasa==2.8.2
    pip install flask
    ```
5. Train the Rasa model:
    ```sh
    rasa train
    ```

## Usage

### Running the Assistant

While you run each command on seperate terminal and start the run

1. Start the Rasa server:
    ```sh
    rasa run
    ```
2. Start the Rasa actions server:
    ```sh
    rasa run actions
    ```
3. Start the Flask server:
    ```sh
    python app.py
    ```

4. Open your browser and go to `http://localhost:5000` to interact with the assistant.

## Configuration
- `config.yml`: Rasa configuration file.
- `domain.yml`: Contains the domain specification.
- `data/nlu.yml`: Contains NLU training data.
- `data/stories.yml`: Contains training stories.
- `data/rules.yml`: Contains rule-based stories.
- `actions/`: Contains custom action code.