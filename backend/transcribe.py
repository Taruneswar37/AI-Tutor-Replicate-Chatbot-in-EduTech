import whisper
model=whisper.load_model('base')
def transcribe_m(file_name):
    result=model.transcribe(file_name)
    return result["text"]

if __name__=="__main__":
    input=transcribe_m("C:/Users/VARSHINI/Desktop/video text/data/uploads/VID-20250916-WA0017.mp4")
    print(input)    