# My Homelab Services Display App

This is an Electron app that displays the services running in my homelab. The backend of the app is powered by a Flask API. It is primarily designed to show services running on Proxmox, but it can also display any HTTP service.

## Features

- View a list of services running in my homelab
- Get detailed information about each service
- Start, stop, or restart services from the app

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `npm install`.
3. Start the app by running `npm start`.

## Usage

1. Launch the app.
2. The app will automatically fetch the list of services from the Flask API.
3. Browse through the list of services and click on a service to view more details.
4. Use the provided controls to start, stop, or restart a service.

## Backend

The backend of this app is a Flask API that performs the following tasks:

- Monitors the status of various services running in the homelab.
- Fetches and returns the status of Proxmox nodes, containers, and virtual machines.

### Key Components

- `loopServices()`: A function that continuously checks the status of predefined services and updates their status every 60 seconds.
- `/status` endpoint: An API endpoint that returns the status of Proxmox nodes, containers, virtual machines, and the monitored services.

### Environment Variables

- `API_TOKEN_PROXMOX`: The API token used to authenticate with the Proxmox API.

### Running the Backend

1. Ensure you have Python and Flask installed.
2. Set up your environment variables in a `.env` file.
3. Run the Flask app using the command `python app.py`.

The backend will start a thread to monitor the services and will be accessible at `http://0.0.0.0:5000`.

## Technologies Used

- Electron
- Python
- Flask
- HTML
- CSS
- JavaScript

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
