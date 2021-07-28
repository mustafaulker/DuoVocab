FROM python

COPY . /DuoVocab
WORKDIR /DuoVocab

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
