# Password_Manager_python-_app

# Password Manager

The Password Manager is a simple application built with Tkinter that allows users to generate secure passwords and save their website login details securely.

## Password Generator

The Password Generator feature helps users create strong and random passwords consisting of letters, numbers, and symbols. It generates a password of 9 characters length, including 5 letters, 2 symbols, and 2 numbers.

## Save Password

Users can save their website login details by entering the website, email/username, and password in the respective fields and clicking the "Add" button. The application will prompt the user to confirm the details before saving them.

## User Interface (UI) Setup

The UI consists of the following components:
- Website: Entry field for the website URL.
- Email/Username: Entry field for the email address or username associated with the website.
- Password: Entry field for the password.
- Generate Password: Button to generate a secure password.
- Add: Button to save the website login details.
- Logo: Displayed at the top of the window for visual branding.

## Usage

1. Enter the website URL, email/username, and password.
2. Click the "Generate Password" button to create a secure password (optional).
3. Click the "Add" button to save the website login details.
4. Confirm the details in the popup window and click "OK" to save.

## File Storage

The login details are stored in a file named "save_passwords" in the current directory. Each entry consists of the website URL, email/username, and password separated by '|'.

## Dependencies

- Tkinter: Python's standard GUI (Graphical User Interface) toolkit.
- Random module: For generating random characters for the password.
- Messagebox: For displaying messages and confirmation prompts.

