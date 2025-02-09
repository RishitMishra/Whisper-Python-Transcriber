import os
import whisper 

#Current directory - D:\Internship Idea labs

def find_all_media(directory):
    Media_extensions = ('.mp4', '.m4a', '.mp3', '.wav', '.flac', '.aac')
    media_files = []
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.lower().endswith(Media_extensions):
                media_files.append(os.path.join(root,file))
    return media_files

def transcribe_file(files):
    model = whisper.load_model("tiny")
    os.makedirs("Transcriptions", exist_ok=True)
    count = 1
    for file in files:
        try:
            print(f"Transcribing file: {file}")
            result = model.transcribe(file)
            with open(os.path.join("Transcriptions", f"output{count}.txt"), "w") as f:
                f.write(f"transcript for file at '{file}'\n\n{result['text']}")
            count += 1
        except Exception as e:
            print(f"Error transcribing '{file}': {e}")
            return
    print("All files successfully transcripted")

directory = input("Enter folder path:")
media_files = find_all_media(directory)
transcribe_file(media_files)