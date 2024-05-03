# PlanetVideoGamesWebApp
# Planet Video Games

Planet Video Games is a Flask-based web application that allows users to explore, add, and edit video game listings. It features a dynamic interface where users can search for games, view detailed information about each game, and manage game entries through a user-friendly dashboard.

## Features

- **Explore Video Games:** Browse through a list of popular video games on the homepage. This feature allows users to quickly see the most popular games of the week through embedded YouTube trailers and easy navigation to game details.

- **Search Functionality:** Enables users to search for video games based on titles, descriptions, features, and release years. The search results are dynamically updated to show relevant games that match the search criteria, enhancing user experience by providing quick and easy access to the games they're interested in.

- **Add New Games:** Users can add new video game listings to the platform through a detailed form that captures all necessary information about the game, including title, media links, description, year of release, and more.

- **Edit Existing Games:** Provides functionality for users to modify details of existing video game listings. This is especially useful for maintaining up-to-date information and adjusting game details as needed.

- **Responsive Design:** The website is optimized for both desktop and mobile devices, ensuring a seamless user experience across different platforms.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework used for building the backend of the application. It handles routing, requests, and the rendering of HTML templates.

- **Bootstrap:** Utilized for styling and creating responsive design elements such as forms, buttons, and modals, making the website accessible and visually appealing on various devices.

- **jQuery:** Used for handling events, performing AJAX requests, and manipulating the DOM in the client's browser. It simplifies complex operations like sending data to the server without a page refresh.

- **JavaScript:** Empowers interactive elements on the website and improves user interactions by providing dynamic content updates and client-side validations.

## Getting Started

### Prerequisites

- Python 3.6+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mantwi/PlanetVideoGamesWebApp.git
   cd PlanetVideoGamesWebApp
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python server.py
6. Open http://127.0.0.1:5000/ in your web browser.
