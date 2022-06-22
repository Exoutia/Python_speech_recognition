from time import sleep

from api_key import API_KEY

from requests import get
from requests import post

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization': API_KEY}


# upload 

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    # print(upload_response.json())

    audio_url = upload_response.json()["upload_url"]
    return audio_url

# transcription
def transcription(audio_url):
    transcript_request = { "audio_url": audio_url }

    transcript_response =post(transcript_endpoint, json=transcript_request, headers=headers)
    # print(transcript_response.json())
    
    job_id = transcript_response.json()['id']
    
    return job_id



# pulling 
def pull(job_id):
    pulling_endpoint = transcript_endpoint + "/" + job_id
    pulling_response = get(pulling_endpoint, headers=headers)
    # print(pulling_response.json())
    return None

def get_transcription_result(job_id):
    pulling_endpoint = transcript_endpoint + "/" + job_id
    while True:
        pulling_response = get(pulling_endpoint, headers=headers)
        if pulling_response.json()['status'] == 'completed':
            print(pulling_response.json())
            return pulling_response.json()
        elif pulling_response.json()['status'] == 'error':
            print(pulling_response.json())
            return "error"
        print("waiting 30 second...")
        sleep(30)
        

def save_file(data, filename):
    if data == "error":
        print(data)
        return 
    filename_x = filename + ".txt"
    with open(filename_x, 'w') as f:
        f.write(data['text'])
    print(f"files is saved as {filename_x}")
    return filename_x
