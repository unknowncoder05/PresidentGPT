# Define the default goal
.DEFAULT_GOAL := help

# Load environment variables from the .env file
include .env
export $(shell sed 's/=.*//' .env)

# Help command to list available commands
help:
	@echo "Usage:"
	@echo "  make <command>"
	@echo ""
	@echo "Commands:"
	@echo "  build      Build the Docker image"
	@echo "  up         Start the Docker container"
	@echo "  down       Stop the Docker container"
	@echo "  logs       View logs from the Docker container"
	@echo "  bash       Access the container's bash shell"

# Build the Docker image
build:
	docker-compose build

# Start the Docker container
up:
	docker-compose up

# Stop the Docker container
down:
	docker-compose down

# View logs from the Docker container
logs:
	docker-compose logs -f

# Access the container's bash shell
bash:
	docker-compose exec app bash
