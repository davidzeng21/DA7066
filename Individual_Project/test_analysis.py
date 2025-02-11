import unittest
from Individual_Project.data_reader import read_data
from Individual_Project.plot_northernmost_observation import plot_northernmost_observation
from Individual_Project.plot_observations_per_year import plot_observations_per_year
from Individual_Project.plot_weekly_observations import plot_weekly_observations

class TestButterflyAnalysis(unittest.TestCase):

    def test_read_data_valid(self):
        data = read_data('test_data_valid.csv')
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['Artnamn'], 'Butterfly A')
        self.assertEqual(data[1]['Antal'], 2)
        self.assertEqual(data[2]['Nord'], 7000000)

    def test_read_data_invalid(self):
        data = read_data('test_data_invalid.csv')
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['Artnamn'], 'Butterfly A')
        self.assertEqual(data[1]['Antal'], 2)

    def test_plot_northernmost_observation(self):
        data = read_data('test_data_valid.csv')
        plot_northernmost_observation(data)
        # Check if the output file is created
        self.assertTrue(os.path.exists('Butterfly A_northernmost_observation.pdf'))

    def test_plot_observations_per_year(self):
        data = read_data('test_data_valid.csv')
        plot_observations_per_year(data)
        # Check if the output file is created
        self.assertTrue(os.path.exists('Butterfly A_observations_per_year.pdf'))

    def test_plot_weekly_observations(self):
        data = read_data('test_data_valid.csv')
        plot_weekly_observations(data)
        # Check if the output file is created
        self.assertTrue(os.path.exists('Butterfly A_weekly_observations.pdf'))

if __name__ == '__main__':
    unittest.main()
