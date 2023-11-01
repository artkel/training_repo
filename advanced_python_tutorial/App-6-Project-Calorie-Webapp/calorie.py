from temperature import Temperature

class Calorie:
    """
    Represent amount of calories calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        result = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * self.temperature
        return result

if __name__ == "__main__":
    temp = Temperature(country='spain', city='malaga').get()
    calorie = Calorie(weight=68, height=175, age=32, temperature=temp)
    print(calorie.calculate())