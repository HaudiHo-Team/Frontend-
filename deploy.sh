#!/bin/bash

# Deploy script for Streamlit Frontend
set -e

echo "🚀 Starting deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create logs directory
mkdir -p logs

# Copy environment file if it doesn't exist
if [ ! -f .env ]; then
    print_warning ".env file not found. Copying from env.example..."
    cp env.example .env
    print_warning "Please edit .env file with your configuration before running again."
    exit 1
fi

# Build and start services
print_status "Building Docker image..."
docker-compose build --no-cache

print_status "Starting services..."
docker-compose up -d

# Wait for services to be ready
print_status "Waiting for services to start..."
sleep 10

# Check if services are running
if docker-compose ps | grep -q "Up"; then
    print_status "✅ Services are running!"
    print_status "Frontend: http://localhost:8501"
    print_status "Health check: http://localhost:8501/_stcore/health"
else
    print_error "❌ Services failed to start. Check logs with: docker-compose logs"
    exit 1
fi

# Show logs
print_status "Showing recent logs..."
docker-compose logs --tail=20

print_status "🎉 Deployment completed successfully!"
print_status "To view logs: docker-compose logs -f"
print_status "To stop services: docker-compose down"
