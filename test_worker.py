import unittest
class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'



class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("koko", 100, 10)

    def test_initiation_of_worker(self):
        self.assertEqual("koko", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_work_works(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_decrease_energy(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_raise_error(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_rests(self):
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_if_info_is_correct(self):
        self.assertEqual("koko has saved 0 money.", self.worker.get_info())



if __name__ == "__main__":
    main()