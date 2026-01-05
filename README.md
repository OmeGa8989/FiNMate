# FINMATE – Smart Investment Advisory

A Django REST API backend for FINMATE, a smart investment advisory platform that helps users manage their financial transactions and get personalized investment recommendations.

## Features

### 🔐 Authentication Module
- User registration and login using Django's built-in authentication
- Token-based authentication for API access
- Password hashing and validation
- User profile management with risk assessment
- Personal information and investment preferences storage

### 📂 Transaction Management
- CSV/XLSX file upload for transaction data
- Automatic parsing of transaction files using pandas
- Support for various date formats and file structures
- Transaction categorization and analysis
- Real-time upload status tracking
- Data validation and error reporting

### 📊 Analytics & Statistics
- Transaction statistics and summaries
- Monthly spending analysis
- Income vs expense tracking
- Category-wise breakdown
- Investment performance insights

## Project Structure

```
finmate/
├── finmate/                 # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings with API configurations
│   ├── urls.py             # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
├── authentication/         # User authentication app
│   ├── models.py           # User profile and risk profile models
│   ├── serializers.py      # API serializers for authentication
│   ├── views.py            # Authentication API views
│   ├── urls.py             # Authentication URL patterns
│   ├── admin.py            # Admin interface configuration
│   └── signals.py          # User creation signals
├── transactions/           # Transaction management app
│   ├── models.py           # Transaction and upload models
│   ├── serializers.py      # Transaction API serializers
│   ├── views.py            # Transaction API views
│   ├── urls.py             # Transaction URL patterns
│   ├── admin.py            # Transaction admin interface
│   └── utils.py            # File parsing utilities
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | User registration |
| POST | `/api/auth/login/` | User login |
| POST | `/api/auth/logout/` | User logout |
| GET/PUT | `/api/auth/profile/` | Get/update user profile |
| GET/PUT | `/api/auth/profile/details/` | Get/update detailed profile |
| GET/PUT | `/api/auth/profile/risk/` | Get/update risk profile |
| POST | `/api/auth/change-password/` | Change password |
| GET | `/api/auth/dashboard/` | User dashboard data |

### Transaction Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/transactions/` | List/create transactions |
| GET/PUT/DELETE | `/api/transactions/{id}/` | Transaction detail operations |
| POST | `/api/upload/transactions/` | Upload CSV/XLSX files |
| GET | `/api/upload/transactions/history/` | Upload history |
| GET | `/api/upload/transactions/{id}/status/` | Upload status |
| GET | `/api/categories/` | Transaction categories |
| GET | `/api/transactions/stats/` | Transaction statistics |

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd BNP-Hackathon/finmate
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## File Upload Format

### Supported File Types
- CSV (.csv)
- Excel (.xlsx)

### Required Columns
- `date` - Transaction date (various formats supported)
- `description` - Transaction description
- `amount` - Transaction amount (positive for income, negative for expenses)

### Optional Columns
- `reference_number` - Bank reference or transaction ID
- `balance` - Account balance after transaction
- `category` - Transaction category
- `type` - Transaction type

### Example CSV Format
```csv
date,description,amount,reference_number
2024-01-15,Salary Credit,5000.00,TXN123456
2024-01-16,Grocery Shopping,-150.75,TXN123457
2024-01-17,ATM Withdrawal,-200.00,TXN123458
```

## Configuration

### Environment Variables
Key settings in `settings.py`:

- `SECRET_KEY` - Django secret key (change in production)
- `DEBUG` - Debug mode (set to False in production)
- `ALLOWED_HOSTS` - Allowed host names
- `FILE_UPLOAD_MAX_MEMORY_SIZE` - Maximum file upload size (5MB)
- `ALLOWED_TRANSACTION_FILE_EXTENSIONS` - Allowed file types

### Database Configuration
Default: SQLite (suitable for development)
For production, configure PostgreSQL or MySQL in `DATABASES` setting.

## Security Features

- Token-based authentication
- Password validation and hashing
- File type and size validation
- CORS configuration for frontend integration
- XSS and CSRF protection
- SQL injection protection through Django ORM

## Error Handling

The API provides comprehensive error handling:
- File validation errors
- Data parsing errors
- Authentication errors
- Permission errors
- Server errors with detailed messages

## Testing

### Manual Testing with curl

1. **Register a user**
   ```bash
   curl -X POST http://localhost:8000/api/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{
       "username": "testuser",
       "email": "test@example.com",
       "first_name": "Test",
       "last_name": "User",
       "password": "securepassword123",
       "password_confirm": "securepassword123"
     }'
   ```

2. **Login**
   ```bash
   curl -X POST http://localhost:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{
       "username": "testuser",
       "password": "securepassword123"
     }'
   ```

3. **Upload transactions**
   ```bash
   curl -X POST http://localhost:8000/api/upload/transactions/ \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -F "file=@transactions.csv"
   ```

# Gemini Financial Toolkit 📈

This project is a suite of Python scripts that leverage the Google Gemini API to provide powerful financial analysis of your transaction history. It can automatically categorize your spending from an Excel file, generate visual reports, create a personalized financial advisory summary, and help you plan your investments based on your monthly surplus.

## ✨ Features

* **Automatic Transaction Categorization**: Uses the Gemini API to intelligently classify transactions into six distinct categories.
* **Data Visualization**: Generates a pie chart to visualize the distribution of your spending.
* **Financial Summary**: Calculates total income, expenses, and monthly surplus.
* **AI-Generated Advisory Reports**: Creates a friendly, practical financial report with personalized advice on your spending habits.
* **Personalized Portfolio Planning**: Suggests a tailored investment portfolio based on your monthly surplus and chosen risk profile.

---

## 📂 File Descriptions

This repository contains the following key Python scripts:

### `main2.py`
* **Purpose**: The foundational script for transaction classification.
* **Functionality**:
    * Reads an Excel file containing financial transactions.
    * Iterates through each transaction, calling the Gemini API to assign a category.
    * Saves the newly categorized data to a new Excel file.

### `main3.py`
* **Purpose**: An enhanced version of the classifier that adds visualization and summary calculations.
* **Functionality**:
    * Includes all the classification features of `main2.py`.
    * **Adds a pie chart** to visually represent the spending distribution across categories using Matplotlib.
    * Includes a function to calculate total income, total expenses, and the monthly surplus from a classified Excel file.

### `advisory_report.py`
* **Purpose**: The most comprehensive script, providing a qualitative financial analysis.
* **Functionality**:
    * Classifies transactions just like the other scripts.
    * After classification, it summarizes the spending data and sends it back to the Gemini API with a new prompt.
    * **Generates a natural language advisory report** offering insights into spending habits and practical suggestions for financial improvement.

### `portfolio.py`
* **Purpose**: A standalone module for investment planning.
* **Functionality**:
    * Takes your calculated **monthly surplus** and a **risk profile** (Conservative, Moderate, or Aggressive) as input.
    * Generates a personalized investment portfolio, allocating funds across low, medium, and high-risk instruments.
    * Projects the potential 12-month return on investment based on the suggested portfolio.

---

## 🛠️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd gemini

### 2. Install Dependencies
```It's recommended to use a virtual environment.

Bash
```
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install required packages
pip install -r requirements.txt
Create a requirements.txt file with the following content:

pandas
openpyxl
matplotlib
python-dotenv
google-generativeai
### 3. Set Up Environment Variables
```The scripts require a Google Gemini API key.

Create a file named .env in the root of the gemini folder.

Add your API key to this file:

API_KEY="YOUR_GEMINI_API_KEY_HERE"


## Future Enhancements

- Investment recommendation algorithm
- Portfolio analysis
- Risk assessment automation
- Email notifications
- Mobile app integration
- Real-time market data integration
- Machine learning for spending patterns

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is part of the BNP Hackathon and is intended for demonstration purposes." 
