def get_response(mood):
    mood = mood.lower()
    
    if mood == "happy":
        return "Yay! Keep smiling Zindagi khubsoorat hai!"
    elif mood == "sad":
        return "Hey, don't worry. Har raat ke baad subah zaroor hoti hai"
    elif mood == "angry":
        return "Thoda deep breath lo Aur batao kya hua?"
    elif mood == "bored":
        return "Try something new today! Kya tumhe game pasand hai?"
    elif mood == "excited":
        return "Woah! Share your excitement with the world!"
    elif mood == "tired":
        return "Take some rest . Tumhara health sabse important hai."
    else:
        return "Mujhe wo mood samajh nahi aaya Thoda aur explain karo?"
