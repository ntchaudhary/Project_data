import speech_recognition as sr
mic_name = "Microphone (Realtek High Defini"
sample_rate=48000
chunk_size=2048
r=sr.Recognizer()
mic_list=sr.Microphone.list_microphone_names()
for i,microphone_name in enumerate(mic_list):
    if microphone_name==mic_name:
        device_id=i
with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    audio=r.listen(source)
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
