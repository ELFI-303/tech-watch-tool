# Tech Watch Tool

Tech Watch Tool is a Python-based web application designed to scrape, analyze, and present articles from the web. It leverages powerful technologies like Docker, Flask, Playwright, and the Llama 3.2-3B model to provide insights into the latest industry trends. Articles are analyzed for relevance and sorted into categories, giving users an intuitive UI to explore curated content.

## Features

- **Web Scraping**: Uses [Playwright](https://playwright.dev/) for robust, headless web scraping.
- **AI-Powered Analysis**: Implements Llama 3.2-3B for article analysis and categorization.
- **Interactive UI**: Built with [Flask](https://flask.palletsprojects.com/) to display curated content.
- **Containerized Deployment**: Fully Dockerized for ease of deployment and scaling.
- **Automatic Sorting**: Articles are ranked and grouped based on relevance to predefined categories.
- 
## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)


### Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/tech-watch-tool.git
   cd tech-watch-tool

2. **Build and Start the Docker Containers**  
   ```bash
   docker-compose up --build

3. **Access the Application**  
   Open your browser and go to http://localhost:5000.

### Project Structure

  ```
  tech-watch-tool/
  ├── app/
  │   ├── templates/         # HTML templates for the Flask UI
  │   ├── static/            # CSS and JavaScript for the front end
  │   ├── app.py             # Flask application
  │   ├── dockerfile         # Docker python image
  │   └── requierements.txt  # Python depedencies
  ├── ollama/
  │   └── Llama3.2-3B        # Ollama Llama3.2-3b version pulled
  ├── scraper/
  │   ├── analyze/           # Ollama interactions directory
  │   │   └── llm.py         # Ollama requests and prompts functions
  │   ├── tools/             # Tools directory 
  │   │   ├── config.py      # Configuration file with categories defined and other variables
  │   │   └── utils.py       # Diverses tools used in the script
  │   ├── website/  # Tests for scraping functionality
  │   │   ├── rss.py         # Abstract class that define RSS Feed classes, use it to add a new source
  │   │   └── sources.py     # All the data gathering endpoints, can be RSS feed, websites, blogs...
  │   ├── dockerfile         # Docker python image
  │   ├── main.py            # Main of the scraper
  │   └── requierements.txt  # Python depedencies
  ├── docker-compose.yml     # Docker-compose configuration, ollama image, playwright image and redirection to build folders
  ├── entrypoint.sh          # Ollama pull Llama3.2:3b
  └── README.md              # Project documentation  

### Technologies Used

* Docker: For containerized development and deployment.
* Python: Core programming language.
* Playwright: Headless browser automation for scraping.
* Flask: Lightweight web framework for the UI.
* Llama 3.2-3B: State-of-the-art language model for analysis.

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

### Acknowledgments

[Playwright Documentation] (https://playwright.dev/python/docs/intro)
[Flask Documentation] (https://flask.palletsprojects.com/en/latest/)
[Llama Model by Meta AI] (https://www.llama.com/)
