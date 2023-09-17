import os
import sys
import json

from dataclasses import dataclass

from typing import Any

@dataclass
class DataLoader:
    data_path: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        
    def save_data(data: Any) -> None:
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)    
    
    def load_data():
        # TODO: Implement this function
        # Determine how to choose which data to load
        # with open('data.json') as json_file:
        raise NotImplementedError

if __name__ == "__main__":
    print (DataLoader.data_path)
    # save_data([1,2,3,4,5]) 