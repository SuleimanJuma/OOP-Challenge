class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at midpoint
        self.energy = 5   # Starting at midpoint
        self.happiness = 5  # Starting at midpoint
        self.tricks = []  # For bonus feature

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy increased!")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played with you. Energy decreased, but happiness increased!")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        
        # Status messages
        if self.hunger >= 8:
            print(f"{self.name} is very hungry!")
        if self.energy <= 2:
            print(f"{self.name} is very tired!")
        if self.happiness <= 2:
            print(f"{self.name} is feeling sad!")

    # Bonus methods
    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")