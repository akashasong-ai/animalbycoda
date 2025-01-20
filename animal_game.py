import random

# Move the animals dictionary outside of the function
animals = {
    # Mammals
    "elephant": ["I am very big", "I have a long trunk", "I have big ears", "I live in Africa or Asia"],
    "lion": ["I am called the king of the jungle", "I have a mane if I'm a boy", "I roar very loud", "I am a big cat"],
    "tiger": ["I have orange fur with black stripes", "I am a big cat", "I love to swim", "I live in Asia"],
    "giraffe": ["I have a very long neck", "I have spots", "I am very tall", "I eat leaves from trees"],
    "monkey": ["I love bananas", "I can climb trees very well", "I have a long tail", "I am very playful"],
    "kangaroo": ["I have a pouch", "I can jump very high", "I live in Australia", "I carry my babies in my pouch"],
    "panda": ["I am black and white", "I love eating bamboo", "I live in China", "I am a type of bear"],
    "zebra": ["I have black and white stripes", "I look like a horse", "I live in Africa", "I travel in herds"],
    "cheetah": ["I am the fastest land animal", "I have spots", "I live in Africa", "I can run up to 70 mph"],
    "koala": ["I live in Australia", "I eat eucalyptus leaves", "I sleep most of the day", "I am not actually a bear"],
    "hippopotamus": ["I am very heavy", "I love being in water", "I live in Africa", "I have a very big mouth"],
    "rhinoceros": ["I have a horn on my nose", "I have thick skin", "I am very heavy", "I can be very dangerous"],
    "gorilla": ["I am the largest primate", "I live in forests", "I am very strong", "I eat mostly plants"],
    "wolf": ["I hunt in packs", "I am related to dogs", "I howl at the moon", "I have thick fur"],
    "deer": ["I have antlers if I'm a boy", "I can run very fast", "I live in forests", "I eat plants"],
    
    # Birds
    "penguin": ["I cannot fly", "I love to swim", "I walk funny", "I live where it's very cold"],
    "parrot": ["I can talk like humans", "I have colorful feathers", "I have a curved beak", "I can live for many years"],
    "owl": ["I am active at night", "I can turn my head very far", "I am very quiet when I fly", "I am considered wise"],
    "eagle": ["I have very good eyesight", "I am a bird of prey", "I build my nest high up", "I am a symbol of freedom"],
    "peacock": ["I have beautiful tail feathers", "I can spread my tail like a fan", "I have bright colors", "I am quite proud"],
    
    # Reptiles
    "snake": ["I have no legs", "I can be venomous", "I shed my skin", "I flick my tongue to smell"],
    "crocodile": ["I have many sharp teeth", "I live in water and land", "I have scaly skin", "I am a reptile"],
    "turtle": ["I carry my house on my back", "I move very slowly", "I can live very long", "I have a hard shell"],
    "lizard": ["I can lose my tail", "I like to sunbathe", "I have scaly skin", "I can climb walls"],
    "chameleon": ["I can change my color", "I have a long tongue", "I can move my eyes separately", "I am a type of lizard"],

    # Marine Animals
    "dolphin": ["I am very intelligent", "I live in the ocean", "I use echolocation", "I am a mammal that swims"],
    "shark": ["I have many sharp teeth", "I must keep swimming", "I have fins", "I am the ocean's top predator"],
    "whale": ["I am the largest animal", "I live in the ocean", "I breathe through a blowhole", "I sing songs"],
    "octopus": ["I have eight arms", "I can change color", "I am very smart", "I can squeeze into small spaces"],
    "jellyfish": ["I have no bones", "I can glow in the dark", "I can sting", "I am mostly made of water"],

    # ... continuing with more animals and their features
}

def play_animal_game():
    print("Welcome to the Animal Guessing Game!")
    print("I will give you clues about an animal, and you try to guess what it is!\n")

    while True:
        # Pick a random animal
        animal = random.choice(list(animals.keys()))
        clues = random.sample(animals[animal], len(animals[animal]))  # Randomize the order of clues
        
        print("Here are your first clues:")
        # Show clues two at a time
        for i in range(0, len(clues), 2):
            print(f"Clue #{i+1}: {clues[i]}")
            if i+1 < len(clues):
                print(f"Clue #{i+2}: {clues[i+1]}")
            
            guess = input("\nCan you guess what animal I am? ").lower()
            if guess == animal:
                print("🎉 Correct! You're amazing! 🎉")
                break
            elif i+2 < len(clues):  # Only show "Not quite" if there are more clues
                print("Not quite! Here are two more clues...\n")
        
        if guess != animal:
            last_guess = input("\nLast chance! What animal am I? ").lower()
            if last_guess == animal:
                print("🎉 Correct! You're amazing! 🎉")
            else:
                print(f"Sorry! I was a {animal}!")

        play_again = input("\nDo you want to play again? (yes/no) ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Bye bye! 👋")
            break

if __name__ == "__main__":
    play_animal_game() 