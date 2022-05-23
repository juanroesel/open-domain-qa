# Basic open-domain QA system using BERT

## Prerequisites
- Docker

## Instructions
1. Clone the repository into a local folder
```
$ git clone <repo url>
```

2. Download `train`, `dev` and `test` files containing subset of SQUAD data into `/data` folder - [Link to data](https://drive.google.com/drive/folders/1K0gkypdXDnHUZ0c8qgrWbRjN2vJnG4Hj?usp=sharin")

3. Pull project image from Docker Hub:
```
$ docker pull juanroesel/open-domain-QA-BERT
```
4. Launch the container powering the QA prototype application
```
$ docker-compose up
```
