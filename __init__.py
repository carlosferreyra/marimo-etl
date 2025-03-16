"""
marimo-etl package initialization.
This module exposes the API for the marimo-etl project.
"""
class API:
    def __init__(self):
        self.dataset = None
        # Hardcoded list of URLs to fetch data from
        self.urls = [
            "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv",
            "https://raw.githubusercontent.com/datasets/population/master/data/population.csv",
            "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv",
            "https://raw.githubusercontent.com/datasets/inflation/master/data/inflation-annual.csv",
            "https://raw.githubusercontent.com/datasets/employment/master/data/employment-rate.csv"
        ]
        self._fetched_data = None

    def load_dataset(self, path):
        """Load a dataset from the given path"""
        import pandas as pd
        self.dataset = pd.read_csv(path)
        return self.dataset

    def fetch_data_generator(self):
        """Generator to fetch data from URLs one by one to optimize memory usage"""
        import requests

        for url in self.urls:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for HTTP errors
                yield response.text
            except Exception as e:
                yield f"Error fetching {url}: {str(e)}"

    def get(self, index=None):
        """
        Fetch data from URLs and return it

        Parameters:
        -----------
        index : int, optional
            If provided, returns data from the specific URL index
            If None, returns a list with all fetched data

        Returns:
        --------
        str or list
            The fetched data as text string(s)
        """
        import requests

        # Lazy loading - fetch only when requested
        if index is not None:
            # Return data for a specific URL
            if 0 <= index < len(self.urls):
                try:
                    response = requests.get(self.urls[index])
                    response.raise_for_status()
                    return response.text
                except Exception as e:
                    return f"Error fetching {self.urls[index]}: {str(e)}"
            else:
                return f"Index {index} out of range (0-{len(self.urls)-1})"
        else:
            # Use the generator to fetch all data (memory efficient)
            return self.fetch_data_generator()

    def save_to_csv(self, data, filename):
        """Save fetched data to a CSV file"""
        try:
            with open(filename, 'w') as f:
                f.write(data)
            return f"Data saved to {filename}"
        except Exception as e:
            return f"Error saving data: {str(e)}"

# Create an instance of the API class that can be imported
api = API()