import random

# Move the animals dictionary outside of the function
animals = {
    # Mammals
    "dog": ["I am man's best friend", "I bark to communicate", "I love to fetch and play", "I am very loyal to humans"],
    "cat": ["I purr when happy", "I am an independent hunter", "I love to chase mice", "I land on my feet"],
    "horse": ["I have a flowing mane", "I can carry people on my back", "I run very fast", "I live in stables"],
    "cow": ["I give milk", "I say moo", "I have spots or solid colors", "I graze in fields"],
    "pig": ["I love mud baths", "I have a curly tail", "I say oink", "I am very intelligent"],
    "sheep": ["I give wool", "I say baa", "I live in flocks", "I graze in pastures"],
    "goat": ["I can climb mountains", "I have horns", "I eat anything", "I have a beard"],
    "rabbit": ["I have long ears", "I hop around", "I love carrots", "I have a fluffy tail"],
    "squirrel": ["I collect nuts", "I climb trees quickly", "I have a bushy tail", "I prepare for winter"],
    "bear": ["I love honey", "I hibernate in winter", "I can fish for salmon", "I am very strong"],
    "sloth": ["I move very slowly", "I hang upside down", "I live in rainforests", "I sleep most of the day"],
    "leopard": ["I have spotted fur", "I can climb trees", "I hunt at night", "I am a big cat from Africa"],
    "camel": ["I have humps on my back", "I can survive in the desert", "I can go days without water", "I am used for transport"],
    "llama": ["I am related to camels", "I live in South America", "I can spit when angry", "I have soft wool"],
    "bat": ["I fly at night", "I use echolocation", "I sleep upside down", "I am the only flying mammal"],
    "raccoon": ["I have a masked face", "I wash my food", "I am active at night", "I am very clever with my hands"],
    "fox": ["I am a clever hunter", "I have a bushy red tail", "I make yipping sounds", "I live in forests and cities"],
    "skunk": ["I have a white stripe", "I spray a smelly defense", "I am black and white", "I eat insects and plants"],
    "otter": ["I love to swim", "I float on my back", "I use tools to crack shells", "I play in the water"],
    "beaver": ["I build dams", "I have a flat tail", "I cut down trees", "I make homes in rivers"],
    "moose": ["I have huge antlers", "I live in cold forests", "I am the largest deer", "I wade in lakes for water plants"],
    "buffalo": ["I travel in large herds", "I once roamed the plains", "I have curved horns", "I am also called bison"],
    "ferret": ["I am long and slim", "I am a playful pet", "I love to tunnel and explore", "I am related to weasels"],
    "guinea pig": ["I squeak when excited", "I am a popular small pet", "I love fresh vegetables", "I come from South America"],
    "hamster": ["I store food in my cheeks", "I run in a wheel", "I am active at night", "I am a tiny pet rodent"],
    "mouse": ["I am very small", "I love cheese", "I have a long thin tail", "I make people scared"],
    "rat": ["I am bigger than a mouse", "I am very intelligent", "I can swim well", "I live in cities and sewers"],
    "opossum": ["I play dead when scared", "I am a marsupial", "I have a long naked tail", "I come out at night"],
    "armadillo": ["I have armor plates", "I can roll into a ball", "I dig for insects", "I live in the Americas"],
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
    "chicken": ["I lay eggs daily", "I cluck and crow", "I have a red comb on my head", "I live on farms"],
    "duck": ["I quack", "I can swim and fly", "I have webbed feet", "I love bread crumbs"],
    "turkey": ["I gobble", "I have a fan-shaped tail", "I am eaten on Thanksgiving", "I have a snood on my beak"],
    "penguin": ["I cannot fly", "I love to swim", "I walk funny", "I live where it's very cold"],
    "parrot": ["I can talk like humans", "I have colorful feathers", "I have a curved beak", "I can live for many years"],
    "owl": ["I am active at night", "I can turn my head very far", "I am very quiet when I fly", "I am considered wise"],
    "eagle": ["I have very good eyesight", "I am a bird of prey", "I build my nest high up", "I am a symbol of freedom"],
    "falcon": ["I am the fastest flying bird", "I dive for prey", "I have sharp talons", "I am trained for hunting"],
    "swan": ["I have a long graceful neck", "I mate for life", "I am elegant in water", "I have white feathers"],
    "flamingo": ["I stand on one leg", "I am bright pink", "I live in large groups", "I filter feed in water"],
    "pigeon": ["I live in cities", "I coo softly", "I have iridescent neck feathers", "I am called a dove's cousin"],
    "sparrow": ["I am a small brown bird", "I hop while walking", "I live near humans", "I eat seeds and insects"],
    "robin": ["I have a red breast", "I hunt for worms", "I sing early in the morning", "I am a sign of spring"],
    "blue jay": ["I am bright blue", "I am very noisy", "I love acorns", "I can mimic hawk calls"],
    "cardinal": ["I am bright red if male", "I have a crest on my head", "I don't migrate in winter", "I whistle prettily"],
    "woodpecker": ["I drum on trees", "I have a strong beak", "I eat insects in wood", "I have a long sticky tongue"],
    "hummingbird": ["I am very tiny", "I can hover", "I drink nectar", "I have iridescent feathers"],
    "crow": ["I am very smart", "I am all black", "I collect shiny things", "I can use tools"],
    "peacock": ["I have beautiful tail feathers", "I can spread my tail like a fan", "I have bright colors", "I am quite proud"],
    
    # Reptiles & Amphibians
    "snake": ["I have no legs", "I can be venomous", "I shed my skin", "I flick my tongue to smell"],
    "crocodile": ["I have many sharp teeth", "I live in water and land", "I have scaly skin", "I am a reptile"],
    "alligator": ["I look like a crocodile", "I live in swamps", "I have a wider snout", "I am found in America"],
    "turtle": ["I carry my house on my back", "I move very slowly", "I can live very long", "I have a hard shell"],
    "lizard": ["I can lose my tail", "I like to sunbathe", "I have scaly skin", "I can climb walls"],
    "iguana": ["I am a large lizard", "I have spines on my back", "I can swim well", "I love eating plants"],
    "gecko": ["I can walk on ceilings", "I make clicking sounds", "I hunt insects at night", "I have sticky toe pads"],
    "chameleon": ["I can change my color", "I have a long tongue", "I can move my eyes separately", "I am a type of lizard"],
    "frog": ["I start life as a tadpole", "I catch flies with my tongue", "I can jump very far", "I say ribbit"],
    "toad": ["I have warty skin", "I live on land", "I hop rather than jump", "I eat garden pests"],

    # Marine Animals
    "dolphin": ["I am very intelligent", "I live in the ocean", "I use echolocation", "I am a mammal that swims"],
    "shark": ["I have many sharp teeth", "I must keep swimming", "I have fins", "I am the ocean's top predator"],
    "whale": ["I am the largest animal", "I live in the ocean", "I breathe through a blowhole", "I sing songs"],
    "seal": ["I bark like a dog", "I can swim very well", "I have flippers", "I balance balls on my nose"],
    "walrus": ["I have long tusks", "I live in the Arctic", "I am very large", "I rest on ice floes"],
    "octopus": ["I have eight arms", "I can change color", "I am very smart", "I can squeeze into small spaces"],
    "starfish": ["I have five arms", "I can regrow lost limbs", "I live on the seafloor", "I can turn my stomach inside out"],
    "crab": ["I walk sideways", "I have strong claws", "I have a hard shell", "I live on beaches and in water"],
    "lobster": ["I have two large claws", "I can live very long", "I turn red when cooked", "I grow bigger by molting"],
    "jellyfish": ["I have no bones", "I can glow in the dark", "I can sting", "I am mostly made of water"],

    # Insects & Arachnids
    "spider": ["I spin webs", "I have eight legs", "I catch flies", "I can be venomous"],
    "ant": ["I live in colonies", "I am very strong", "I work together", "I build underground homes"],
    "butterfly": ["I start as a caterpillar", "I have colorful wings", "I drink nectar", "I help pollinate flowers"],
    "bee": ["I make honey", "I live in a hive", "I can sting once", "I help pollinate flowers"],
    "ladybug": ["I have spots", "I eat plant pests", "I bring good luck", "I am red and black"],
    "dragonfly": ["I have four wings", "I fly very fast", "I catch insects", "I live near water"],
    "mosquito": ["I buzz in ears", "I drink blood", "I can spread disease", "I breed in water"],
    "worm": ["I live in soil", "I help plants grow", "I have no legs", "I come out when it rains"],
    "snail": ["I carry my shell", "I move very slowly", "I leave a slimy trail", "I have eye stalks"],
    
    # Fish
    "goldfish": ["I am a common pet", "I have a short memory", "I am orange or gold", "I live in bowls or ponds"],
    "koi": ["I am colorful", "I live in ponds", "I am from Japan", "I can live for many years"],
    "carp": ["I am a large fish", "I live in fresh water", "I am bottom feeder", "I am related to goldfish"],
    "betta fish": ["I have flowing fins", "I fight other males", "I make bubble nests", "I am very colorful"],
    "clownfish": ["I live in sea anemones", "I am orange and white", "I can change gender", "I was in Finding Nemo"],
    "seahorse": ["I swim upright", "Males carry babies", "I hold with my tail", "I change color to hide"],
    "ray": ["I am flat", "I glide through water", "I have a long tail", "I am related to sharks"],
    "eel": ["I look like a snake", "I can make electricity", "I live in deep water", "I am long and slippery"],
    
    # Fish
    
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