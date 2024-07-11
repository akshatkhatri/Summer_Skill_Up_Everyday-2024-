class Bank:
    def __init__(self, name, age, balance : float = 0) -> None:
        self.name = name
        self.age = age
        self.balance = balance

    def __str__(self) -> str:
        return (f"{self.name} is of age {self.age} and has balance of {self.balance} ")

    def __add__(self,other) -> "Bank":
        joint_name = f"Joint Owners are -> {self.name} & {other.name}"
        joint_age = self.age + other.age
        joint_balance = self.balance + other.balance

        return Bank(joint_name, joint_age, joint_balance)


def main():
    akshat = Bank("Akshat",19,60000)
    ishita = Bank("Ishita",20,45000)

    print(akshat)
    print(ishita)

    joint_ak_is = akshat + ishita

    print(joint_ak_is)


if __name__ == "__main__":
    main()