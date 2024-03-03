import unittest

from module_03_ci_culture_beginning.homework.hw3.accounting import app, storage


class Accounting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        storage.update(
            {
                2000: {
                    1: 2,
                    2: 6,
                    3: 10,
                    4: 14,
                    5: 18,
                    6: 22,
                    7: 26,
                    8: 30,
                    9: 34,
                    10: 38,
                    11: 42,
                    12: 46,
                    "total": 288,
                }
            }
        )
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        cls.app = app.test_client()
        cls.base_url = "/"

    def test_add_data_in_response(self):
        self.base_url += "add/"
        data_int = 20000115
        expense_int = 1123
        response = self.app.get(self.base_url + str(data_int) + "/" + str(expense_int))
        response_str = response.data.decode()
        expected_data = "-".join(
            [str(data_int)[0:4], str(data_int)[4:6], str(data_int)[6:8]]
        )
        self.assertIn(expected_data, response_str)

    def test_add_expense_in_response(self):
        self.base_url += "add/"
        data_int = 20000115
        expense_int = 1123
        response = self.app.get(self.base_url + str(data_int) + "/" + str(expense_int))
        response_str = response.data.decode()
        expected_expense = str(expense_int)
        self.assertIn(expected_expense, response_str)

    def test_add_correct_data_in_storage(self):
        self.base_url += "add/"
        data_int = 20000115
        expense_int = 1123
        response = self.app.get(self.base_url + str(data_int) + "/" + str(expense_int))
        response_str = response.data.decode()
        year = int(str(data_int)[0:4])
        month = int(str(data_int)[4:6])
        add_year = storage.get(year, False)
        add_month = storage[year].get(month, False)
        self.assertTrue(add_year)
        self.assertTrue(add_month)

    def test_add_correct_total_in_storage(self):
        self.base_url += "add/"
        data_int = 20000115
        year = int(str(data_int)[0:4])
        before_total = storage[year].get("total", False)
        expense_int = 100
        response = self.app.get(self.base_url + str(data_int) + "/" + str(expense_int))
        # response_str = response.data.decode()
        add_total = storage[year].get("total", False)
        self.assertEqual(add_total, before_total + expense_int)

    def test_add_incorrect_date(
        self,
    ):  # тут тесты срабатывают если я в коде уберу try exept
        with self.assertRaises(ValueError):
            self.base_url += "add/"
            data_int = "ymd"
            expense_int = 133
            response = self.app.get(
                self.base_url + str(data_int) + "/" + str(expense_int)
            )
            response_str = response.data.decode()
            print(response_str)

    def test_calculate_year(self):
        self.base_url = "/calculate/"
        year_int = 2000
        response = self.app.get(self.base_url + str(year_int))
        response_str = response.data.decode()
        self.assertIn(str(year_int), response_str)
        self.assertIn("3757", response_str)

    def test_calculate_month(self):
        self.base_url = "/calculate/"
        year_int = 2000
        month_int = 1
        response = self.app.get(self.base_url + str(year_int) + "/" + str(month_int))
        response_str = response.data.decode()
        self.assertIn(str(year_int), response_str)
        self.assertIn("3471", response_str)

    def test_clear_storage_year(self):
        storage.clear()
        self.base_url = "/calculate/"
        year_int = 2000
        response = self.app.get(self.base_url + str(year_int))
        response_str = response.data.decode()
        self.assertIn(str(year_int), response_str)
        self.assertIn("<b>0</b> ", response_str)

    def test_clear_storage_month(self):
        storage.clear()
        self.base_url = "/calculate/"
        year_int = 2000
        month_int = 1
        response = self.app.get(self.base_url + str(year_int) + "/" + str(month_int))
        response_str = response.data.decode()
        self.assertIn(str(year_int), response_str)
        self.assertIn("<b>0</b> ", response_str)
