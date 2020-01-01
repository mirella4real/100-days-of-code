import boto3

polly = boto3.client('polly',
    region_name='us-east-1',
    aws_access_key_id='...',
    aws_secret_access_key='...')

result = polly.synthesize_speech(Text='Hello World!',
    OutputFormat='mp3',
    VoiceId='Aditi')

audio = result['AudioStream'].read()
with open("helloworld.mp3", "wb") as file:
    file.write(audio)