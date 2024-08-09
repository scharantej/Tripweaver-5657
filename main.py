
from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # Get travel details
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        departure_date = request.form.get('departure_date')
        return_date = request.form.get('return_date')

        # Fetch search results
        # NOTE: Replace the API keys with your own
        flights_api_key = 'YOUR_API_KEY'
        hotels_api_key = 'YOUR_API_KEY'
        activities_api_key = 'YOUR_API_KEY'

        flights_url = 'https://example.com/flights'
        hotels_url = 'https://example.com/hotels'
        activities_url = 'https://example.com/activities'

        flights_params = {'origin': origin, 'destination': destination, 'departure_date': departure_date, 'return_date': return_date}
        hotels_params = {'destination': destination, 'arrival_date': departure_date, 'departure_date': return_date}
        activities_params = {'destination': destination, 'start_date': departure_date, 'end_date': return_date}

        flights_response = requests.get(flights_url, params=flights_params)
        hotels_response = requests.get(hotels_url, params=hotels_params)
        activities_response = requests.get(activities_url, params=activities_params)

        # Store search results in session
        session['flights'] = flights_response.json()
        session['hotels'] = hotels_response.json()
        session['activities'] = activities_response.json()

        # Redirect to results page
        return redirect(url_for('results'))

    return render_template('index.html')

@app.route('/results')
def results():
    # Retrieve search results from session
    flights = session.get('flights')
    hotels = session.get('hotels')
    activities = session.get('activities')

    return render_template('results.html', flights=flights, hotels=hotels, activities=activities)

if __name__ == '__main__':
    app.run(debug=True)
