# PresidentGPT

This project leverages OpenAI's API to simulate gathering and summarizing opinions from U.S. presidents based on a given prompt. The application uses Docker for containerization and requires certain Python packages for execution.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Usage

1. **Run the application using Docker:**

   ```sh
   make up
   ```

2. **Or run the application locally:**

   ```sh
   python main.py
   ```

## Files

- **.gitignore**: Specifies files and directories to be ignored by Git.
- **docker-compose.yml**: Defines services, networks, and volumes for Docker.
- **Dockerfile**: Instructions to build a Docker image for the application.
- **main.py**: The main script containing the logic to gather and summarize opinions from U.S. presidents.
- **makefile**: A file containing a set of directives used with the `make` build automation tool.
- **presidents.json**: A JSON file containing data about U.S. presidents.
- **requirements.txt**: Lists the Python packages required to run the application.

## Configuration

- **DEFAULT_COUNTRY**: The default country, set to "USA".
- **PRESIDENT_DATA_JSON_FILE**: The JSON file containing presidents' data (`presidents.json`).
- **TEMP_DATA_FILE**: The temporary file to save opinions (`.data/temp.json`).
- **AMOUNT_OF_PRESIDENTS**: The number of presidents to gather opinions from, set to 2 by default.

### Example `presidents.json`

Ensure your `presidents.json` file is formatted correctly. Here's an example structure:

```json
[
    {
        "name": "George Washington"
    },
    {
        "name": "Thomas Jefferson"
    }
]
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`.
5. Push to the branch: `git push origin feature/your-feature-name`.
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.