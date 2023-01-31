import argparse
import time
import pygame
from tqdm import tqdm

def main(session_minutes=25, break_minutes=5, rounds=5):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load sound file
    sound = pygame.mixer.Sound("sounds/sound.wav")
    
    victory = pygame.mixer.Sound("sounds/victory.wav")

    for i in range(rounds):
        # Start timer
        for j in tqdm(range(session_minutes*60), desc='Session', bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}'):
            time.sleep(1)

        # Play sound for 5 seconds
        sound.play()
        time.sleep(5)
        sound.stop()

        if i < rounds-1:
            # Take a break
            for j in tqdm(range(break_minutes*60), desc='Break', bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}'):
                time.sleep(1)

            # Play sound for 5 seconds
            sound.play()
            time.sleep(5)
            sound.stop()
    victory.play()
    print("Pomodoro completed!")
    time.sleep(8)
    victory.stop()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pomodoro Timer app')
    parser.add_argument('session_minutes', type=int, nargs='?', default=20, help='Session time in minutes')
    parser.add_argument('break_minutes', type=int, nargs='?', default=5, help='Break time in minutes')
    parser.add_argument('rounds', type=int, nargs='?', default=10, help='Number of rounds')
    parser.add_argument('--session_minutes', type=int, dest='session_minutes', help='Session time in minutes')
    parser.add_argument('--break_minutes', type=int, dest='break_minutes', help='Break time in minutes')
    parser.add_argument('--rounds', type=int, dest='rounds', help='Number of rounds')
    args = parser.parse_args()
    main(session_minutes=args.session_minutes, break_minutes=args.break_minutes, rounds=args.rounds)
