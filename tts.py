from gradio_client import Client, file
import os
import shutil

# Initialize the client with the URL of your Gradio app (of GPT So VIT)
client = Client("http://localhost:9872/")

def generate(text):
    # Prompt the user for input paths and text
    audio_path = r"" # Your voice sample
    transcription_text = "" # Your voice sample's transcription
    additional_text = text

    print(audio_path, transcription_text, additional_text)

    # Define other parameters as needed // Don't worry about the french, may need to addapt it for your language tho
    prompt_language = "Anglais"
    text_language = "Anglais"
    how_to_cut = "Découpez par des points en anglais"
    top_k = 30
    top_p = 0.85
    temperature = 0.5
    ref_free = False
    speed = 1.1
    if_freeze = False
    inp_refs = None

    # Make the API call
    result = client.predict(
        ref_wav_path=file(audio_path),
        prompt_text=transcription_text,
        prompt_language=prompt_language,
        text=additional_text,
        text_language=text_language,
        how_to_cut=how_to_cut,
        top_k=top_k,
        top_p=top_p,
        temperature=temperature,
        ref_free=ref_free,
        speed=speed,
        if_freeze=if_freeze,
        inp_refs=inp_refs,
        api_name="/get_tts_wav"
    )

    # Define the target save path
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get script directory
    output_path = os.path.join(script_dir, "output_audio.wav")  # Define output file name

    # Move the generated file to the script directory
    shutil.move(result, output_path)

    print("The resulting audio file is saved at:", output_path)
    return output_path