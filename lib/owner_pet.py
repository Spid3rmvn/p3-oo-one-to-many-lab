class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception(
                f"Invalid pet type. Must be one of: {', '.join(self.PET_TYPES)}"
            )
        self.pet_type = pet_type

        # Set owner if provided
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            self.owner = owner
        else:
            self.owner = None

        # Add to all pets list
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of all pets owned by this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to this owner"""
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
