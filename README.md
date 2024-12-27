# **Medicine Search API**

A RESTful API built with **Python** and **Flask** for managing and retrieving information about medicines. This API provides endpoints to fetch all medicines, search by name, and retrieve details of specific medicines using their unique ID.

---

## **Features**
- Retrieve all medicines stored in the database.
- Search medicines by name with case-insensitive and prefix-based filtering.
- Fetch detailed information about a specific medicine using its ID.
- Lightweight and easy to deploy, suitable for integration with web or mobile applications.

---

## **Endpoints**

### 1. **Get All Medicines**
**Endpoint**:  
`GET /api/v1/medicines`

**Description**:  
Returns a list of all medicines in the database.

**Response**:  
```json
[
    {
        "id": 1,
        "name": "Augmentin 625 Duo Tablet",
        "manufacturer_name": "Glaxo SmithKline Pharmaceuticals Ltd",
        "price(₹)": 223.42,
        "pack_size_label": "strip of 10 tablets",
        "short_composition1": "Amoxycillin (500mg)",
        "short_composition2": "Clavulanic Acid (125mg)",
        "type": "allopathy",
        "Is_discontinued": false
    },
]
```

### 2. **Seach Medicine by Name**
**Endpoint**:  
`GET /api/v1/medicines/<name of medicine>`

**Description**:  
Returns a list of all medicines in the database.

**Response**:  
```json
[
    {
        "id": 1,
        "name": "Augmentin 625 Duo Tablet",
        "manufacturer_name": "Glaxo SmithKline Pharmaceuticals Ltd",
        "price(₹)": 223.42,
        "pack_size_label": "strip of 10 tablets",
        "short_composition1": "Amoxycillin (500mg)",
        "short_composition2": "Clavulanic Acid (125mg)",
        "type": "allopathy",
        "Is_discontinued": false
    }
]
```
### 3. **Seach Medicine by ID**
**Endpoint**:  
`GET /api/v1/medicines/<Id number of medicine>`

**Description**:  
Returns a list of all medicines in the database.

**Response**: 
```json
{
    "id": 1,
    "name": "Augmentin 625 Duo Tablet",
    "manufacturer_name": "Glaxo SmithKline Pharmaceuticals Ltd",
    "price(₹)": 223.42,
    "pack_size_label": "strip of 10 tablets",
    "short_composition1": "Amoxycillin (500mg)",
    "short_composition2": "Clavulanic Acid (125mg)",
    "type": "allopathy",
    "Is_discontinued": false
}
```
### **Error response**
**If medicine does not exist a `404` is returned.
```json
{
    "error": "Medicine not found"
}
```
### **Steps to Run Locally**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jaanu2505/indian_medicines_api.git
    ```
2. **Navigate to the project directory**:
   ```bash
   cd indian_medicines_api
   ```
3. **Install Dependencies: Use pip to install the required dependencies listed in the `requirement.txt` file.***
   ```bash
   pip install -r requirement.txt
   ```
4. **Run the Application: Start the Flask development server:**
   ```bash
   python api.py
   ```
5. **Access the API: Open your browser or use a tool like Postman to visit:**
    ```bash
    http://127.0.0.1:5000
    ```
### **Technologies Used**
- **Python**: Core programming language for building the API.
- **Flask**: Lightweight web framework for creating RESTful APIs.
- **Pandas**: Library for efficient data manipulation and querying.

## **Prerequisites**

- **Python**: Version 3.8 or higher.
- **Pip**: Python's package installer.
- **Git**: For cloning the repository.
- A basic understanding of Python and REST APIs (optional but helpful).

