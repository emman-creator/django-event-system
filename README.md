# Event Management System

This project is a Django-based **Event Management System** that allows users to create, edit, delete, and filter events by category. It features an intuitive interface and easy-to-use forms for managing events efficiently.

## Features

- **Home Page**: Displays a list of all events with options to filter by category.
- **Create Event**: Allows users to add new events with fields like title, description, date, time, location, and category.
- **Edit Event**: Enables users to update existing event details.
- **Delete Event**: Provides an option to delete events with a confirmation popup.
- **Filter by Category**: Lets users view events filtered by predefined categories.

## Screenshots

### Home Page
<img width="655" height="421" alt="image" src="https://github.com/user-attachments/assets/fb7bcd8d-e414-4737-9749-a2dded33d2d4" />


## Project Structure

### Files

- **`models.py`**
  - Defines the `Event` model with fields such as `title`, `description`, `date`, `time`, `location`, and `category`.
  - Includes category options like `Social`, `Workshop`, `Meetup`, `Conference`, and `Other`.

- **`views.py`**
  - Handles logic for displaying, creating, editing, deleting, and filtering events.
  - Contains functions:
    - `displayEvents`: Displays all events.
    - `createEvent`: Handles creating new events.
    - `editEvent`: Handles updating existing events.
    - `deleteEvent`: Deletes an event.
    - `filterEvent`: Filters events by category.

- **`urls.py`**
  - Maps URLs to corresponding views.
  - Routes include:
    - `/`: Home page.
    - `/create/`: Create a new event.
    - `/edit/<id>/`: Edit an event.
    - `/delete/<id>/`: Delete an event.
    - `/category/<category>/`: Filter events by category.

### Templates

- **`home.html`**: Displays all events with options to filter by category.
- **`form.html`**: Provides a form for creating or editing events.
