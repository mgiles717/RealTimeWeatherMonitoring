import modules.pyweather as pyweather
import utils.utils as utils


def main():
    weather = pyweather.get_weather("New York")
    print(weather)

if __name__ == "__main__":
    main()