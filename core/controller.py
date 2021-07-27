import io
import time
import requests
from common.utils import Document


def recommend_content(filepath):
    document = Document(filepath)
    return document.read()
