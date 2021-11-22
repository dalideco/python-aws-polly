import os
from dotenv import load_dotenv
import boto3

load_dotenv()

ACCESS_KEY_ID= os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY=os.getenv('SECRET_ACCESS_KEY')

polly= boto3.client('polly',
    region_name= 'eu-central-1',
    # Keys="dalideco_accessKeys.csv"
    aws_access_key_id= ACCESS_KEY_ID,
    aws_secret_access_key= SECRET_ACCESS_KEY
)

result = polly.synthesize_speech(
    Text="Hello World!",
    OutputFormat="mp3",
    VoiceId="Matthew"
)

audio = result['AudioStream'].read()

with open("helloworld.mp3","wb") as file:
    file.write(audio)

