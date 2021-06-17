# SynthMPDGenerator

SynthMPDGenerator is a tool for generating synthetic mobile positioning data based on cell location data. This tool was developed by employees of Positium while on a Development Week.

## Usage

Change the values in config.yaml to fit your own parameters and run the main.py file in the directory using your preferred method for running python scripts (e.g. bash):

```bash
python3 main.py
```

This will generate 3 files: a call detail records file (in cdr_files/), a cell locations file (in cell_location_files/) and a metadata file containing the meaningful locations for users and their profiles (in metadata_files/).

## Workflow

The script for generating mobile positioning data works as follows:
- Generate a cell network based on the input cell location data.
- Generate a population of users. For each user:
    - Generate the correct profile (ATM this is just generalized for the whole population).
    - Generate meaningful locations (home, work, regular cells).
    - Generate mobile positioning data based on the following trends:
        - Activity differences between weekdays (e.g. more activity on Mondays than on Saturdays).
        - Activity differences between times of day (e.g. more activity at 5 PM than 3 AM).
        - Location trends depending on time of day (e.g more likely to be at work during the day than at home and the other way around during the night).
- Concatenate every user's mobile positioning data to the population's mobile positioning data.
- Export output files: mobile positioning data, cell location data and metadata.


## Config

All of the parameters in the config can be left as default, but you can tune them to your own liking to generate data with different densities and patterns in time and space.

## Input data

At the moment, Estonian cells data from opencellid.org is bundled with this repo as input data and synthetic mobile positioning data can be generated based on that. However, this script can be used on any country's cell location data.

## Future plans
- Assign weights to cell locations with differing levels of clustering (so that places with higher clustering are more likely chosen).
- Implement a decent way of choosing work and regular cells from home cells.
- Add a way to use different weekend configurations.
- Implement some kind of model (e.g. HMM) for predicting where a person might be depending on the time of day.
- Optimise the hell out of the algorithm.