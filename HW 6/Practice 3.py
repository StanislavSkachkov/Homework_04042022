class Worker:
    name = "Иван"
    surname = "Иванов"
    position = "CEO"
    _income = {"wage":1000000, "bonus":25000000}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname


    def get_total_income(self):
        return sum(self._income.values())


worker_1 = Position ()
print (worker_1.get_full_name())
print (worker_1.get_total_income())
