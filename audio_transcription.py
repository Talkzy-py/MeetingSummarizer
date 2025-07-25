import whisper

model = whisper.load_model("base", device="cuda")
print("Using device: ", model.device)

result = model.transcribe("test_audio.mp3")
print(result['text'])
