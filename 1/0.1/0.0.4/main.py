import whisper  # Alternative for speech_recognition
#import conversation1
#import gtts  # Alternative for pyttsx3
#import openApplication
import sounddevice as sd  # For handling audio input/output
import numpy as np
import warnings

#suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

model = whisper.load_model("base")
#model = whisper.load_model("tiny")

SILENCE_THRESHOLD = 0.01
SILENCE_DURATION = 1


def get_audio():
    print("Speak")

    sample_rate = 16000
    buffer_size = sample_rate //2  # Record in 0.5 second chunks
    silence_counter = 0
    audio_data = []

    #record in chunks
    def callback(indata, frames, time, status):
        nonlocal silence_counter
        if status:
            print(status)

        volume_norm = np.linalg.norm(indata) * 10
        audio_data.append(indata.copy()) 

        #if the volume is below threshold, start counting silence
        if volume_norm < SILENCE_THRESHOLD:
            silence_counter +=1
        else:
            silence_counter = 0 
        
        #stop after a duration of silence
        if silence_counter > SILENCE_DURATION * (sample_rate/buffer_size):
            raise sd.CallbackStop()
        
    #record using until silence is detected
    with sd.InputStream(samplerate=sample_rate, channels=1, callback=callback):
        sd.sleep(30000) #large sleep to keep the stream open, will be interrupted by silence
    
    audio = np.concatenate(audio_data, axis=0).flatten()

    #recongnise the speech
    result = model.transcribe(audio, language='en')
    said = result['text'].strip().lower()

    print('You said:', said)


get_audio()
