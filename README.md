# FarmDash

## Description

FarmDash is a web application designed to streamline farm management tasks. It provides features for monitoring various metrics related to farm operations, such as animal health and environmental conditions. This project aims to assist farmers in efficiently managing their farms by providing real-time data visualization and analysis.

## Installation

To get started with FarmDash, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository>
   cd <repository>
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Optionally, run tests:
   ```bash
   python manage.py test
   ```

Now, you can access FarmDash in your web browser at `http://localhost:8000`. Enjoy managing your farm efficiently with FarmDash!
