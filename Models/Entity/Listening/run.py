import pyaudio
import wave
from gtts import gTTS
import os

def record_audio(file_name, duration=10):
    p = pyaudio.PyAudio()
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    
    inputDeviceIndex = 4 #Microphone
    # inputDeviceIndex = 2 #Mac Mic
    # input_device_index=4,

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    input_device_index=inputDeviceIndex,
                    frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    print('opening',file_name)
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

                text = recognizer.recognize_wav(audio_data, sample_rate=sample_rate)


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('response.mp3')
    os.system('start response.mp3')

if __name__ == "__main__":
    try:
        while True:
            record_audio('input.wav')  # Record audio stream
            # Add your processing logic here (e.g., speech-to-text, NLP)
            response_text = "This is a response."  # Replace with actual response logic
            text_to_speech(response_text)  # Convert response to speech
    except KeyboardInterrupt:
        print("Program terminated.")
