# Address Book Application

The Address Book Application is a simple Python program that allows you to manage your contacts. You can add, list, update, and delete contact information using this application. Contacts are stored in an SQLite database.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Adding a Contact](#adding-a-contact)
  - [Listing Contacts](#listing-contacts)
  - [Updating a Contact](#updating-a-contact)
  - [Deleting a Contact](#deleting-a-contact)
  - [Exiting the Application](#exiting-the-application)

## Getting Started

### Prerequisites

- Python (version 3.x)
- SQLite (usually included with Python)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/michaelc143/address_book.git
```

2. Navigate to the project directory

```bash
cd address-book
```

3. Run the application
```bash
python address_book.py
```

## Usage


### Adding a Contact

- Choose option 1 from the menu.
- Enter the name and email address of the contact.
- The contact will be added to the database, and a success message will be displayed.

### Listing Contacts

- Choose option 2 from the menu.
- All stored contacts will be displayed, including their IDs, names, and email addresses.

### Updating a Contact

- Choose option 3 from the menu.
- Enter the contact ID you want to update.
- Enter the updated name and email address for the contact.
- The contact information will be updated, and a success message will be displayed.

### Deleting a Contact

- Choose option 4 from the menu.
- Enter the contact ID you want to delete.
- The contact will be deleted from the database, and a success message will be displayed.

### Exiting the Application

- Choose option 5 from the menu to exit the application.
