import unittest
import os
from data_reader import read_data
from plot_northernmost_observation import plot_northernmost_observation
from plot_observations_per_year import plot_observations_per_year
from plot_weekly_observations import plot_weekly_observations

# Test class for butterfly analysis
class TestButterflyAnalysis(unittest.TestCase):

    def test_read_data_valid(self): # test for valid data
        data = read_data('gronsnabbvinge.csv')
        self.assertEqual(len(data), 21288)
        self.assertEqual(data[0]['Artnamn'], 'Grönsnabbvinge')
        self.assertEqual(data[1]['Antal'], 2)
        self.assertEqual(data[2]['Nord'], 6731180)

    def test_read_data_invalid(self): # test for invalid data
        data = read_data('amiral.csv')
        self.assertEqual(len(data), 41875)
        self.assertEqual(data[0]['Artnamn'], 'Amiral')
        self.assertEqual(data[1]['Antal'], 1)

    def test_plot_northernmost_observation(self): # test for plot northernmost observation
        data = read_data('gronsnabbvinge.csv')
        plot_northernmost_observation(data)
        # Check if the output file is created
        self.assertTrue(os.path.exists('Grönsnabbvinge_northernmost_observation.pdf'))

    def test_plot_observations_per_year(self): # test for plot observations per year
        data = read_data('gronsnabbvinge.csv')
        plot_observations_per_year(data)
        # Check if the output file is created
        self.assertTrue(os.path.exists('Grönsnabbvinge_observations_per_year.pdf'))

    def test_plot_weekly_observations(self): # test for plot weekly observations
        data = read_data('gronsnabbvinge.csv')
        plot_weekly_observations(data)
        # Check if the output file is created
        self.assertTrue(os.path.exists('Grönsnabbvinge_weekly_observations.pdf'))

if __name__ == '__main__':
    unittest.main()
