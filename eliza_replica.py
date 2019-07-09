# A very simple version of ELIZA. Works best if you do most of the talking.
# More info: https://en.wikipedia.org/wiki/ELIZA

import random

def response(chat):

    if "i need" in chat:
        r1 = "Why do you need that?"
        r2 = "Would it really help you if you got it?"
        r3 = "Are you sure you need that"
        return random.choice([r1, r2, r3])
        
    elif "why don't you" in chat:
        r1 = "Do you really think I don't?"
        r2 = "Well, perhaps eventually I will."
        r3 = "Do you really want me to?"
        return random.choice([r1, r2, r3])
        
    elif "why can't i" in chat:
        r1 = "Do you think that I should be able to?"
        r2 = "If you could, what would you do?"
        r3 = "I don't know... why can't you?"
        r4 = "Have you really tried?"
        return random.choice([r1, r2, r3, r4])
        
    elif "i am" in chat:
        r1 = "Is that why you came to me?"
        r2 = "How long have you been like that?"
        r3 = "How do you feel about being like that?"
        return random.choice([r1, r2, r3])
        
    elif "i'm" in chat:
        r1 = "How does being like that make you feel?"
        r2 = "Do you enjoy being like that?"
        r3 = "Why did you tell me that?"
        r4 = "Why do you think you are?"
        return random.choice([r1, r2, r3, r4])

    elif "are you" in chat:
        r1 = "Why does it matter that I am like that?"
        r2 = "Would you prefer it if I were not like that?"
        r3 = "Perhaps you just believe that."
        r4 = "I may be like that... what do you think?"
        return random.choice([r1, r2, r3, r4])

    elif "what" in chat:
        r1 = "Why do you ask?"
        r2 = "How would an answer to that help you?"
        r3 = "What do you think?"
        return random.choice([r1, r2, r3])

    elif "how" in chat:
        r1 = "How do you suppose?"
        r2 = "Perhaps you can answer your own question."
        r3 = "What is it you're really asking?"
        return random.choice([r1, r2, r3])

    elif "because" in chat:
        r1 = "Is that the real reason?"
        r2 = "What other reasons come to mind?"
        r3 = "Does that reason apply to anything else?"
        r4 = "If that's the case, what else must be true?"
        return random.choice([r1, r2, r3, r4])

    elif "sorry" in chat:
        r1 = "There are many times when no apology is needed."
        r2 = "What feelings do you have when you apologize?"
        return random.choice([r1, r2])

    elif "hello" in chat:
        r1 = "Hello... I'm glad you could drop by today."
        r2 = "Hi there... how are you today?"
        r3 = "Hello, how are you feeling today?"
        return random.choice([r1, r2, r3])

    elif "i think" in chat:
        r1 = "Is there any doubt in your mind?"
        r2 ="Do you really think so?"
        r3 = "But you're not sure?"
        return random.choice([r1, r2, r3])

    elif "friend" in chat:
        r1 = "Tell me more about your friends."
        r2 = "When you think of a friend, what comes to mind?"
        r3 = "Why don't you tell me about a childhood friend?"
        return random.choice([r1, r2, r3])

    elif "yes" in chat:
        r1 = "You seem quite sure."
        r2 = "Ok, but can you elaborate a bit?"
        return random.choice([r1, r2])

    elif "computer" in chat:
        r1 = "Are you really talking about me?"
        r2 = "Does it seem strange to talk to a computer?"
        r3 = "How do computers make you feel?"
        r4 = "Do you feel threatened by computers?"
        return random.choice([r1, r2, r3, r4])

    elif "is it" in chat:
        r1 = "Do you think it is?"
        r2 = "Perhaps it is... what do you think?"
        r3 = "If it were, what would you do?"
        r4 = "That could well be the case."
        return random.choice([r1, r2, r3, r4])

    elif "it is" in chat:
        r1 = "You seem very certain."
        r2 = "If I told you that it probably isn't, how would you feel?"
        return random.choice([r1, r2])

    elif "can you" in chat:
        r1 = "What makes you think I can't?"
        r2 = "If I could, then what?"
        r3 = "Why do you ask if I can?"
        return random.choice([r1, r2, r3])

    elif "can i" in chat:
        r1 = "Perhaps you don't want to do that."
        r2 = "Do you want to be able to do that?"
        r3 = "If you could do that, would you?"
        return random.choice([r1, r2, r3])

    elif "you are" in chat:
        r1 = "Why do you think that I am?"
        r2 = "Does it please you to think that I am?"
        r3 = "Perhaps you would like me to be."
        r4 = "Perhaps you're really talking about yourself?"
        return random.choice([r1, r2, r3, r4])

    elif "you're" in chat:
        r1 = "Why do you say that I am?"
        r2 = "Does it please you to think that I am?"
        r3 = "Are we talking about you, or me?"
        return random.choice([r1, r2, r3])

    elif "i don't" in chat:
        r1 = "Don't you really?"
        r2 = "Why don't you?"
        r3 = "Do you want to?"
        return random.choice([r1, r2, r3])

    elif "i feel" in chat:
        r1 = "Good, tell me more about these feelings."
        r2 = "Do you often feel that way?"
        r3 = "When do you usually feel that way?"
        r4 = "When you feel that way, what do you do?"
        return random.choice([r1, r2, r3, r4])

    elif "i have a " in chat:
        r1 = "Maybe you should consult a professional."
        r2 = "Why do you tell me that?"
        r3 = "What do you plan on doing about it?"
        return random.choice([r1, r2, r3])

    elif "i have an " in chat:
        r1 = "Maybe you should consult a professional."
        r2 = "Why do you tell me that?"
        r3 = "What do you plan on doing about it?"
        return random.choice([r1, r2, r3])

    elif "i have" in chat:
        r1 = "Why do you tell me that?"
        r2 = "Have you really?"
        r3 = "What will you do next?"
        return random.choice([r1, r2, r3])

    elif "i would" in chat:
        r1 = "Could you explain to me why you would?"
        r2 = "Why would you?"
        r3 = "Who else knows that you would?"
        return random.choice([r1, r2, r3])

    elif "is there" in chat:
        r1 = "Do you think that there is?"
        r2 = "It's likely that there is."
        r3 = "Would you like there to be?"
        return random.choice([r1, r2, r3])

    elif "my" in chat:
        r1 = "I see..."
        r2 = "Why do you say that?"
        r3 = "And how does this make you feel?"
        return random.choice([r1, r2, r3])

    elif "you" in chat:
        r1 = "We should be discussing you, not me."
        r2 = "Why do you say that about me?"
        r3 = "Why do you care about *me*?"
        return random.choice([r1, r2, r3])

    elif "why" in chat:
        r1 = "Why don't you tell me the reason why?"
        r2 = "Why do you think?"
        return random.choice([r1, r2])

    elif "i want" in chat:
        r1 = "What would it mean to you if you got that?"
        r2 = "Why do you want that?"
        r3 = "What would you do if you got that?"
        r4 = "If you got that, then what would you do?"
        return random.choice([r1, r2, r3, r4])

    elif "mother" in chat:
        r1 = "Tell me more about your mother."
        r2 = "What was your relationship with your mother like?"
        r3 = "How do you feel about your mother?"
        r4 = "How does this relate to your feelings today?"
        r5 = "Good family relations are important."
        return random.choice([r1, r2, r3, r4, r5])

    elif "father" in chat:
        r1 = "Tell me more about your father."
        r2 = "How did your father make you feel?"
        r3 = "How do you feel about your father?"
        r4 = "Does your relationship with your father relate to your feelings today?"
        r5 = "Do you have trouble showing affection with your family?"
        return random.choice([r1, r2, r3, r4, r5])

    elif "child" in chat:
        r1 = "Did you have close friends as a child?"
        r2 = "What is your favourite childhood memory?"
        r3 = "Do you remember any dreams or nightmares from childhood?"
        r4 = "Did the other children sometimes tease you?"
        r5 = "How do you think your childhood experiences relate to your feelings today?"
        return random.choice([r1, r2, r3, r4, r5])

    elif "?" in chat:
        r1 = "Why do you ask that?"
        r2 = "Please consider whether you can answer your own question."
        r3 = "Perhaps the answer lies within yourself."
        r4 = "Why don't you tell me?"
        return random.choice([r1, r2, r3, r4])

    else:
        r1 = "Please tell me more."
        r2 = "Let's change focus a bit... Tell me about your family."
        r3 = "Can you elaborate on that?"
        r4 = "Why do you say that?"
        r5 = "I see..."
        r6 = "Very interesting."
        r7 = "I see. And what does that tell you?"
        r8 = "How does that make you feel?"
        r9 = "How do you feel when you say that?"
        return random.choice([r1, r2, r3, r4, r5, r6, r7, r8, r9])

def run():

    print("Hello, I am a replica of ELIZA, the computer psychotherapist. Please, describe your problems.")
    print("When you feel like you're finished, just type 'quit' and press enter.")
    print("How are you feeling today?")

    while True:
        chat = str(input("> ")).lower()
        if chat == "quit":
            break
        else:
            print(response(chat))

    print("Thank you for talking with me. Goodbye.")
