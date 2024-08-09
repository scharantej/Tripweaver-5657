## Flask Application Design for Travel Planner

### HTML Files
- **index.html**:
  - Displays the main page with a form for entering travel details.
  - Includes Bootstrap CSS and JavaScript for styling and interactivity.
  - Uses Jinja templating to display form fields and errors (if any).
- **results.html**:
  - Displays the search results, including a list of available flights, hotels, and activities.
  - Uses Bootstrap tables and cards for formatting and display.
  - Includes JavaScript for filtering and sorting search results.

### Routes
- **main** (GET):
  - Renders the `index.html` file to display the main page.
- **search** (POST):
  - Processes the travel details submitted via the form on `index.html`.
  - Queries external APIs (e.g., Google Flights, Booking.com) to fetch search results.
  - Stores the results in a session and redirects to `results.html`.
- **results** (GET):
  - Retrieves the search results from the session and renders the `results.html` file to display them.