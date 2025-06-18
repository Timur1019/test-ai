import unittest
from generate_sales_script import generate_sales_script

class TestSalesScriptGenerator(unittest.TestCase):
    def test_script_generation(self):
        script = generate_sales_script()
        self.assertIn("Приветствие", script)
        self.assertIn("Выявление потребности", script)
        self.assertIn("Предложение решения", script)
        self.assertIn("Закрытие", script)
        print("✅ Скрипт успешно сгенерирован")

if __name__ == "__main__":
    unittest.main()
