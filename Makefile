# Makefile for Frontend Application

.PHONY: help build up down logs clean test lint format health

# Default target
help:
	@echo "Available commands:"
	@echo "  build     - Build Docker image"
	@echo "  up        - Start services"
	@echo "  down      - Stop services"
	@echo "  logs      - Show logs"
	@echo "  clean     - Clean up containers and images"
	@echo "  test      - Run tests"
	@echo "  lint      - Run linter"
	@echo "  format    - Format code"
	@echo "  health    - Check health status"
	@echo "  deploy    - Deploy application"

# Build Docker image
build:
	docker-compose build --no-cache

# Start services
up:
	docker-compose up -d

# Stop services
down:
	docker-compose down

# Show logs
logs:
	docker-compose logs -f

# Clean up
clean:
	docker-compose down -v
	docker system prune -f

# Run tests
test:
	docker-compose run --rm frontend python -m pytest tests/

# Run linter
lint:
	docker-compose run --rm frontend flake8 src/

# Format code
format:
	docker-compose run --rm frontend black src/
	docker-compose run --rm frontend isort src/

# Check health
health:
	curl -f http://localhost:8501/health || echo "Health check failed"

# Deploy
deploy:
	./deploy.sh

# Development mode
dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

# Production mode
prod:
	docker-compose --profile production up -d