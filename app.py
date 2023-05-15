import openai
from music21 import converter
from midi2audio import FluidSynth

openai.api_key = "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"
openai.organization = "org-Y6SEavpjn8GFtEJs9UYDNz5B"


def generate_music(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate a music composition in ABC notation that best suits as a background music for the following scenario: {prompt}",
        max_tokens=500,
        n=5,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def abc_to_midi(abc_notation, output_filename):
    music_score = converter.parse(abc_notation, format="abc")
    music_score.write("midi", fp=output_filename)


def midi_to_audio(midi_filename, audio_filename):
    fs = FluidSynth("C:/Users/Hp/Documents/Music/FluidR3Mono_GM.sf3")
    fs.midi_to_audio(midi_filename, audio_filename)


prompt = input("Enter a prompt for music generation: ")
abc_notation = generate_music(prompt)
print("Generated ABC notation:", abc_notation)
# Convert ABC notation to a MIDI file
midi_filename = "generated_music.mid"
abc_to_midi(abc_notation, midi_filename)

# Convert MIDI file to an audio file (MP3 or WAV)
audio_filename = "generated_music.mp3"
midi_to_audio(midi_filename, audio_filename)
print(f"Generated audio file: {audio_filename}")
