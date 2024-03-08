## README (English)

---

### PYTHON PROJECT
**Cohort 6 Data**

**Deadline: 03/14/2023**

---

### Objective
The objective of this project is to process a file containing data and store the data in a chosen data structure (list, tuple, dictionary, or a combination of these). The data file can be accessed [here](https://drive.google.com/drive/folders/1O0CRYR2EZC_ZiQxWH0JOOzQ_XH69nRM).

---

### Tasks
1. **Data Processing:**
   - Separate valid data from invalid data. A line is considered invalid if any of its information is not valid. Keep the information that made it invalid for invalid lines.
   - The data includes:
     - **Number:** Consists of uppercase letters and digits, with a length of 7 characters (e.g., H5G32YR or 54YTG5T).
     - **First Name:** Starts with a letter and contains at least 3 letters.
     - **Last Name:** Starts with a letter and contains at least 2 letters.
     - **Date of Birth:** Must be a valid date. Choose a date format and transform all dates to this format.
     - **Class:** From 6th to 3rd grade, plus letters A, B, C, and D. Choose a class format and transform all classes to this format.
     - **Grade:** The string contains:
       - Different subjects separated by a hash `#`.
       - Grades of subjects within square brackets `[]`.
       - Grades of assignments are separated by the exam grade by two colons `:`.
       - Assignment grades are separated by a vertical bar `|`.
       - Example: `Math[12|11:13]#Francais[4|11|8:13]#Anglais[13,5|11:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]`

2. **Menu Creation:**
   - Display information (valid or invalid; user's choice).
   - Display information by its number.
   - Display the first five entries.
   - Add information by verifying the validity of the given information.
   - Modify invalid information and then transfer it to the structure where valid information is stored.

3. **Pagination Display:**
   - Paginate by 5 lines in the first case.
   - In the second case, ask the user how many lines they want to paginate by.

---

### Note
- Detailed algorithm should be created before starting the Python code.
- Basic Python modules can be used.

---
