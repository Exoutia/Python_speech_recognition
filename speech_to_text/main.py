import json
import requests
from config import API_KEY

from api_comunicate import upload, transcription, get_transcription_result, save_file

import sys

filename = sys.argv[1]


audio_url = upload(filename)
job_id = transcription(audio_url)
data = get_transcription_result(job_id)
filename_save = save_file(data, filename);
