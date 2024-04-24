# Books api

Jest to prosta aplikacja do zarządzania książkami.
Aplikacja pozwala na dodawanie oraz przeglądanie książek.

To przykładowa apliakcja, która należy wdrożyć na AWS.

## Lambda
Do wdrożenia aplikacji na AWS wykorzystano funkcję lambda.
Jest to funkcja triggerowana zapytaniem HTTP. 

## Zmienne środowiskowe
Aplikacja wykorzystuje zmienne środowiskowe, które należy ustawić w AWS.

- `BOOKS_AWS_ACCESS_KEY_ID`
- `BOOKS_AWS_SECRET_ACCESS_KEY`
- `BOOKS_AWS_REGION`
- `BOOKS_TABLE_NAME`
- `BOOKS_QUEUE_URL`
- `BOOKS_IMAGE_API_URL`

Przykładowy sposób ustawienia zmiennych środowiskowych:

```bash
export BOOKS_AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export BOOKS_AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export BOOKS_AWS_REGION=us-east-1
export BOOKS_TABLE_NAME=books-dev
export BOOKS_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/043026380068/new-book
export BOOKS_IMAGE_API_URL=https://n24eaac7mr3xcxccasboewsit40atznr.lambda-url.us-east-1.on.aws
````

Uwaga: Aby uniknąć przekazywania access key, secret acccess key oraz regionu, można użyć odpowiedniego Service Account. 


## Pipeline

```bash
make test
```

```bash
make lint
```

Aby utworzyć plik `app.zip` należy wykonać polecenie:

```bash
make build
```

Powyższy plik, należy wgrać na AWS jako funkcję lambda.


