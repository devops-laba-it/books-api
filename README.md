# Books API

Books API is a simple book management application that allows users to add and browse books. This is a demonstration application designed for deployment on AWS.

## Features

- **Add Books**: Users can add new book records to the database.
- **Browse Books**: Users can view a list of all books available.

## Deployment

This application utilizes AWS Lambda for deployment, which is triggered by HTTP requests.

## Environment Variables

The application requires setting environment variables in AWS:

- `BOOKS_AWS_ACCESS_KEY_ID`: AWS access key ID.
- `BOOKS_AWS_SECRET_ACCESS_KEY`: AWS secret access key.
- `BOOKS_AWS_REGION`: AWS region where the service is hosted.
- `BOOKS_TABLE_NAME`: Name of the DynamoDB table used.
- `BOOKS_QUEUE_URL`: URL of the SQS queue.
- `BOOKS_IMAGE_API_URL`: URL to fetch images from AWS Lambda.

Example of setting environment variables:

```bash
export BOOKS_AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export BOOKS_AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export BOOKS_AWS_REGION=us-east-1
export BOOKS_TABLE_NAME=books-dev
export BOOKS_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/043026380068/new-book
export BOOKS_IMAGE_API_URL=https://n24eaac7mr3xcxccasboewsit40atznr.lambda-url.us-east-1.on.aws
```

**Note**: To avoid explicitly passing AWS credentials and region, consider using an appropriate Service Account.

## Continuous Deployment Pipeline

### Automated Deployment

The application is set up with a continuous deployment pipeline that automatically deploys to AWS Lambda upon every push to the `main` branch. The deployment includes the following steps:

1. **Testing**:
   Run tests to ensure that the recent changes pass all checks.
   ```bash
   make test
   ```

2. **Linting**:
   Perform linting to ensure code quality.
   ```bash
   make lint
   ```

3. **Building**:
   Create the deployable `app.zip` file.
   ```bash
   make build
   ```

4. **Deployment**:
   Upload the `app.zip` file to AWS Lambda.

Ensure that AWS credentials and all required environment variables are set correctly for the deployment script to execute without issues.
