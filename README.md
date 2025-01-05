# Diabetes Prediction Project

This project is a web application for predicting the likelihood of diabetes based on various health parameters. It uses a machine learning model to make predictions and provides a user-friendly interface for inputting health metrics.

## Features

- Home page with an introduction to the tool
- About page with detailed information about diabetes
- Prediction form for inputting health metrics
- Display of prediction results

## Technologies Used

- Django
- Pandas
- Scikit-learn
- HTML/CSS
- JavaScript

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/diabetes-prediction.git
    cd diabetes-prediction
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

5. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Project Structure

```
DiabetesPrediction/
├── DiabetesPrediction/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── view.py
│   ├── wsgi.py
├── static/
│   ├── css/
│   │   ├── style.css
│   ├── images/
│   │   ├── hospital-acquired-nosocomial-infections_thumb.avif
│   │   ├── images.jpg
├── template/
│   ├── about.html
│   ├── home.html
│   ├── predict.html
├── manage.py
├── requirements.txt
└── README.md
```

## Usage

1. Navigate to the home page to get an introduction to the tool.
2. Go to the About page to learn more about diabetes.
3. Use the Predict page to input health metrics and get a prediction result.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
