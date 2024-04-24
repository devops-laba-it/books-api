import json
import os
import uuid

import awsgi
import boto3
from flask import Flask, render_template, request

app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.environ.get("BOOKS_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("BOOKS_AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("BOOKS_AWS_REGION")
TABLE_NAME = os.environ.get("BOOKS_TABLE_NAME")
queue_url = os.environ.get("BOOKS_QUEUE_URL")
IMAGE_API_URL = os.environ.get("BOOKS_IMAGE_API_URL")

sqs = boto3.client(
    service_name="sqs",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

dynamodb = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

table = dynamodb.Table(TABLE_NAME)


class Book:
    def __init__(self, id, title, author, url):
        self.id = id if id else str(uuid.uuid4())
        self.title = title
        self.author = author
        self.url = url


def send_to_queue(book: Book):
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageBody=json.dumps(book.__dict__),
    )

    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        author = request.form["author"]
        title = request.form["title"]

        url = url if url else "https://picsum.photos/2000"

        book = Book(id=None, title=title, author=author, url=url)

        table.put_item(
            Item={
                "id": book.id,
                "author": book.author,
                "title": book.title,
            }
        )

        response = send_to_queue(book)
        print(response)

        return render_template("index.html", book=book)

    return render_template("index.html")


@app.route("/books")
def all_books():
    books = []
    for item in table.scan().get("Items"):
        print(item)
        id = item.get("id")
        book = Book(
            id=id,
            title=item.get("title"),
            author=item.get("author"),
            url=get_image_url(id),
        )
        books.append(book)
    return render_template("all_books.html", books=books)


def get_image_url(book_id):
    return f"{IMAGE_API_URL}/{book_id}.jpg"


def lambda_handler(event, context):
    event["httpMethod"] = event["requestContext"]["http"]["method"]
    event["path"] = event["requestContext"]["http"]["path"]
    event["queryStringParameters"] = event.get("queryStringParameters", {})

    return awsgi.response(app, event, context)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
