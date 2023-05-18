from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os,sys

app=Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    try:
        raise Exception ("we are tasting our customfile")
        
    except Exception as e:
        abc = CustomException(e,sys)
        logging.info(abc.error_message)
        return "Hellow welcome to my project"


if __name__ == "__main__":
    app.run(debug=True)