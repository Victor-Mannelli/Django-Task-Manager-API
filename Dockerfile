FROM python:3.11-alpine

WORKDIR /app

# Install bash, postgresql client, and other necessary packages using apk
RUN apk add --no-cache bash postgresql-client make gcc musl-dev postgresql-dev

# Copy all files to the /app directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PORT=8000
ENV DATABASE_URL=$DATABASE_URL
ENV SECRET_KEY=$SECRET_KEY
ENV DEBUG=$DEBUG

EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]