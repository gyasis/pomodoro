import argparse
from pydub import AudioSegment

def convert_mp3_to_wav(input_file, output_file):
    # open the input mp3 file and convert to wave format
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format="wav")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert mp3 to wav file")
    parser.add_argument("input_file", help="input mp3 file")
    parser.add_argument("output_file", help="output wav file")
    args = parser.parse_args()
    convert_mp3_to_wav(args.input_file, args.output_file)
