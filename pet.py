class Pet:
    def __init__(self, name):  # Runs once when the pet is created
        self.name = name    # String.
        self.age = 1        # Always starts at 1.
        self.mood = 50      # From 0, very sad, to 100, very happy.
        self.hunger = 50    # From 100, very starving, to 0, full.
        self.thirst = 50    # From 100, parched, to 0, quenched.

        # Permanent ASCII art
        self.ascii_art = r"""
        (\_/)
        (•_•)
        />🍪
        """

    def watch_pet(self):
        print(self.ascii_art)

    def play(self):
        print(f"{self.name} is playing...")
        self.mood += 20
        if self.mood > 100:
            self.mood = 100

    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0

    def drink(self):
        print(f"{self.name} is drinking...")
        self.thirst -= 20
        if self.thirst < 0:
            self.thirst = 0

    def status(self):
        print(f"""
              --- {self.name}'s Status ---
              Age: {self.age}
              Mood: {self.mood}
              Hunger: {self.hunger}
              Thirst: {self.thirst}
              """)