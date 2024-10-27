'''
@author:Zhijian Yin
'''
import pandas as pd
import numpy as np
import gc
import json
import os

#### Define the path of the dataset ####
OUTPUT_FOLDER = 'dataset/data/'
AV_ROAD_TEST_FOLDER = 'dataset/CD80_dataset/AV Road Test Data/'
SELF_DRIVING_CRASH_FOLDER = 'dataset/CD80_dataset/Human-Driving and AV Crash Data/Self-Driving Crash Datasets/'
HUMAN_DRIVER_BEHAVIOR_FOLDER = 'dataset/CD80_dataset/Human-Driving and AV IoT Data/Human Driver IoT Datasets/Driver Behavior Dataset/'
POLID_DRIVING_FOLDER='dataset/CD80_dataset/Human-Driving and AV IoT Data/Human Driver IoT Datasets/Polidriving Dataset/'
SELFDRIVING_IOT_FOLDER = 'dataset/CD80_dataset/Human-Driving and AV IoT Data/Self-Driving IoT Datasets/comma2k19_sampled/'
INSUANRANE_CLAIMS_FOLDER = 'dataset/CD80_dataset/Insurance Claims Data/'

#### Functions ####
def AV_road_test_data_process():
    """
    Processes autonomous vehicle road test data for the years 2021, 2022, and 2023.
    This function performs the following steps:
    1. Reads mileage data from CSV files for each year and appends them to a list.
    2. Renames the columns of the mileage data to a consistent format.
    3. Concatenates the mileage data from all years into a single DataFrame.
    4. Reads disengagement data from CSV files for each year and stores them in a dictionary.
    5. Concatenates the disengagement data from all years into a single DataFrame.
    6. Drops rows and columns with all NaN values from both mileage and disengagement DataFrames.
    7. Drops the 'Unnamed: 9' column from the disengagement DataFrame.
    8. Saves the processed mileage and disengagement data to CSV files.
    Note:
    - The function assumes the existence of the following global variables:
    - AV_ROAD_TEST_FOLDER: The folder path where the input CSV files are located.
    - OUTPUT_FOLDER: The folder path where the output CSV files will be saved.
    - The input CSV files should be named in the format '{year}/{year}-Autonomous-Mileage-Reports-CSV.csv' 
    and '{year}/{year}-Autonomous-Vehicle-Disengagements-Reports-CSV.csv'.
    - The encoding for reading the CSV files is set to 'ISO-8859-1'.
    Returns:
    None
    """
    years=[2021,2022,2023]
    mileage_list = []
    for year in years:
        mileage_df = pd.read_csv(AV_ROAD_TEST_FOLDER+f'{year}/{year}-Autonomous-Mileage-Reports-CSV.csv',encoding='ISO-8859-1')
        mileage_df['Year'] = year
        mileage_df.rename(columns={
            f'DEC {year-1}': 'Month 0',
            f'JAN {year}': 'Month 1',
            f'FEB {year}': 'Month 2',
            f'MAR {year}': 'Month 3',
            f'APR {year}': 'Month 4',
            f'MAY {year}': 'Month 5',
            f'JUN {year}': 'Month 6',
            f'JULY {year}': 'Month 7',
            f'AUG {year}': 'Month 8',
            f'SEP {year}': 'Month 9',
            f'OCT {year}': 'Month 10',
            f'NOV {year}': 'Month 11',
            f'DEC {year}': 'Month 12'
        }, inplace=True)
        mileage_list.append(mileage_df)
    Mileage = pd.concat(mileage_list)
    disengagements_dict = {}
    for year in years:
        disengagements_dict[year] = pd.read_csv(AV_ROAD_TEST_FOLDER+f'{year}/{year}-Autonomous-Vehicle-Disengagements-Reports-CSV.csv', encoding='ISO-8859-1')
        disengagements_dict[year]['Year'] = year
    Disengagements = pd.concat([disengagements_dict[year] for year in years])
    Mileage.dropna(how='all',axis=0,inplace=True)
    Mileage.dropna(how='all',axis=1,inplace=True)
    Disengagements.dropna(how='all',axis=0,inplace=True)
    Disengagements.dropna(how='all',axis=1,inplace=True)
    Disengagements.drop(columns=['Unnamed: 9'],inplace=True)
    Mileage.to_csv(OUTPUT_FOLDER+'AVTEST_Mileage.csv',index=False)
    Disengagements.to_csv(OUTPUT_FOLDER+'AVTEST_Disengagements.csv',index=False)

def Selfdriving_crash_data_process():
    """
    Processes self-driving crash data from ADAS and ADS incident reports.

    This function reads two CSV files containing incident reports for Advanced Driver Assistance Systems (ADAS) 
    and Automated Driving Systems (ADS), adds a 'Type' column to each DataFrame to indicate the source of the data, 
    concatenates the DataFrames, and writes the combined data to a new CSV file.

    The input files are expected to be located in the directory specified by the `SELF_DRIVING_CRASH_FOLDER` variable:
    - 'SGO-2021-01_Incident_Reports_ADAS.csv'
    - 'SGO-2021-01_Incident_Reports_ADS.csv'

    The output file is written to the directory specified by the `OUTPUT_FOLDER` variable:
    - 'Selfdriving_Crash.csv'

    Note:
        The CSV files are read with the encoding 'ISO-8859-1'.

    Raises:
        FileNotFoundError: If any of the input files are not found.
        IOError: If there is an issue reading from or writing to the files.
    """
    adas=pd.read_csv(SELF_DRIVING_CRASH_FOLDER+'SGO-2021-01_Incident_Reports_ADAS.csv',encoding='ISO-8859-1')
    adas['Type']='ADAS'
    ads=pd.read_csv(SELF_DRIVING_CRASH_FOLDER+'SGO-2021-01_Incident_Reports_ADS .csv',encoding='ISO-8859-1')
    ads['Type']='ADS'
    selfdriving_crash=pd.concat([adas,ads])
    selfdriving_crash.to_csv(OUTPUT_FOLDER+'Selfdriving_Crash.csv',index=False)

def Human_driver_behavior_data_process():
    """
    Processes human driver behavior data by merging and renaming sensor data files, 
    interpolating missing values, and labeling the data with ground truth events.

    The function performs the following steps:
    1. Merges and renames columns of sensor data files (linear acceleration, acceleration, 
       magnetometer, and gyroscope) from specified repositories.
    2. Interpolates missing values in the merged data using linear interpolation.
    3. Labels the merged data with ground truth events based on the 'groundTruth.csv' file 
       and 'viagem.json' file in each repository.
    4. Concatenates the labeled datasets from multiple repositories into a single DataFrame.
    5. Saves the final processed DataFrame to a CSV file.

    Returns:
        None
    """
    def merge_rename(repo):
        files=['aceleracaoLinear_terra.csv','acelerometro_terra.csv','campoMagnetico_terra.csv','giroscopio_terra.csv']
        files=[repo+'/'+file for file in files]
        linear_acceleration=pd.read_csv(HUMAN_DRIVER_BEHAVIOR_FOLDER+files[0],encoding='ISO-8859-1')
        linear_acceleration.rename(columns={'timestamp':'timestamp','x':'linear_acceleration_x','y':'linear_acceleration_y','z':'linear_acceleration_z'},inplace=True)
        acceleration=pd.read_csv(HUMAN_DRIVER_BEHAVIOR_FOLDER+files[1],encoding='ISO-8859-1')
        acceleration.rename(columns={'timestamp':'timestamp','x':'acceleration_x','y':'acceleration_y','z':'acceleration_z'},inplace=True)
        magnetometer=pd.read_csv(HUMAN_DRIVER_BEHAVIOR_FOLDER+files[2],encoding='ISO-8859-1')
        magnetometer.rename(columns={'timestamp':'timestamp','x':'magnetometer_x','y':'magnetometer_y','z':'magnetometer_z'},inplace=True)
        gyroscope=pd.read_csv(HUMAN_DRIVER_BEHAVIOR_FOLDER+files[3],encoding='ISO-8859-1')
        gyroscope.rename(columns={'timestamp':'timestamp','x':'gyroscope_x','y':'gyroscope_y','z':'gyroscope_z'},inplace=True)
        merged = pd.merge(linear_acceleration, acceleration, on=['timestamp', 'uptimeNanos'], how='outer')
        merged = pd.merge(merged, magnetometer, on=['timestamp', 'uptimeNanos'], how='outer')
        merged = pd.merge(merged, gyroscope, on=['timestamp', 'uptimeNanos'], how='outer')
        # interpolate missing values using linear combination of the previous and latter data
        merged.interpolate(method='linear', inplace=True, limit_direction='both')
        return merged
    def label(repo,merged):
        ground_truth=pd.read_csv(HUMAN_DRIVER_BEHAVIOR_FOLDER+repo+'/groundTruth.csv',encoding='ISO-8859-1')
        with open(HUMAN_DRIVER_BEHAVIOR_FOLDER + repo + '/viagem.json', 'r', encoding='ISO-8859-1') as f:
            viagem = pd.json_normalize(json.load(f))
        start=viagem['firstCollectionUptimeNanos'].iloc[0]
        merged['seconds'] = merged['uptimeNanos'].apply(lambda x: (x - start)/1E9)
        def get_label(seconds):
            for _, row in ground_truth.iterrows():
                if row[' inicio'] <= seconds <= row[' fim']:
                    return row['evento']
            return 'Unknown'

        merged['evento'] = merged['seconds'].apply(get_label)
        return merged
    inner_repos=['16','17','20','21']
    datasets=[]
    for repo in inner_repos:
        merged=merge_rename(repo)
        merged=label(repo,merged)
        datasets.append(merged)
    human_driver_behavior=pd.concat(datasets)
    human_driver_behavior.to_csv(OUTPUT_FOLDER+f'Human_Driver_Behavior.csv',index=False)
   
def Polidriving_data_process():
    """
    Processes driving data for multiple drivers and saves the combined dataset to a CSV file.
    This function performs the following steps:
    1. Defines a list of driver names.
    2. Defines a nested function `get_files` to retrieve file paths for each driver.
    3. Defines a nested function `get_data` to read CSV files and append driver information.
    4. Iterates over each driver name, retrieves file paths, reads data, and appends it to a list.
    5. Concatenates all driver datasets into a single DataFrame.
    6. Saves the combined dataset to a CSV file named 'Polidriving_drivers.csv'.
    7. Reads a labeled dataset from a specific file and saves it to a CSV file named 'Polidriving_labeled.csv'.
    Note:
    - The function assumes the existence of certain global variables: `POLID_DRIVING_FOLDER` and `OUTPUT_FOLDER`.
    - The labeled data file is read with a specific encoding ('ISO-8859-1').
    Returns:
    None
    """
    names=['alonso', 'andres', 'pablo', 'richard', 'yolanda', 'furious']
    def get_files(name):
        paths=[]
        for filepath,dirnames,filenames in os.walk(POLID_DRIVING_FOLDER+name):
            for filename in filenames:
                if '_pre.csv' in filename:
                    paths.append(filepath+'/'+filename)
        return paths
                    
    def get_data(name,paths):
        datasets=[]
        for path in paths:
            data=pd.read_csv(path)
            data['driver']=name
            datasets.append(data)
        return datasets
    datasets=[]
    for name in names:
        paths=get_files(name)
        datasets+=get_data(name,paths)
    polidriving=pd.concat(datasets)
    polidriving.to_csv(OUTPUT_FOLDER+'Polidriving_drivers.csv',index=False)
    labeled_data=pd.read_csv(POLID_DRIVING_FOLDER+'labeled/20240208_120000_lss.csv',encoding='ISO-8859-1')
    labeled_data.to_csv(OUTPUT_FOLDER+'Polidriving_labeled.csv',index=False)

def Selfdriving_IOT_data_process():
    """
    Processes self-driving IoT data from multiple segments and organizes it into a single CSV file.
    This function reads processed log data from various sensors and CAN bus data, organizes it into 
    pandas DataFrames, and merges them into a single DataFrame. The final data is saved as a CSV file.
    The function performs the following steps:
    1. Reads processed log data from specified segments.
    2. Organizes the data into pandas DataFrames.
    3. Merges the DataFrames on the 'timestamp' column.
    4. Interpolates missing values.
    5. Saves the merged data into CSV files for each chunk.
    6. Combines the CSV files from all chunks into a single CSV file.
    7. Removes the intermediate CSV files.
    Returns:
        None
    """
    def read_processed_log(segment):
        data = {}
        log_types = {
            'IMU/accelerometer': ['forward_acceleration', 'right_acceleration', 'down_acceleration'],
            'IMU/gyro_uncalibrated': ['forward_gyro_uncalibrated', 'right_gyro_uncalibrated', 'down_gyro_uncalibrated'],
            'IMU/gyro_bias': ['forward_gyro_bias', 'right_gyro_bias', 'down_gyro_bias'],
            'IMU/gyro': ['forward_gyro', 'right_gyro', 'down_gyro'],
            'IMU/magnetometer_uncalibrated': ['forward_magnetic_uncalibrated', 'right_magnetic_uncalibrated', 'down_magnetic_uncalibrated'],
            'IMU/magnetometer': ['forward_magnetic', 'right_magnetic', 'down_magnetic'],
            'CAN/speed': ['car_speed_m/s'],
            'CAN/steering_angle': ['steering_angle_deg'],
            'CAN/wheel_speeds': ['wheel_speed_front_left', 'wheel_speed_front_right', 'wheel_speed_rear_left', 'wheel_speed_rear_right'],
            'CAN/radar': ['radar_forward_distance', 'radar_left_distance', 'radar_relative_speed', 'radar_nan1', 'radar_nan2', 'radar_address', 'radar_new_track'],
            'GNSS/live_gnss_qcom': ['gnss_qcom_latitude', 'gnss_qcom_longitude', 'gnss_qcom_speed', 'gnss_qcom_utc_timestamp', 'gnss_qcom_altitude', 'gnss_qcom_bearing'],
            'GNSS/live_gnss_ublox': ['gnss_ublox_latitude', 'gnss_ublox_longitude', 'gnss_ublox_speed', 'gnss_ublox_utc_timestamp', 'gnss_ublox_altitude', 'gnss_ublox_bearing'],
        }
        
        for log_type, columns in log_types.items():
            t_path = os.path.join(segment, f'processed_log/{log_type}/t')
            value_path = os.path.join(segment, f'processed_log/{log_type}/value')
            
            if os.path.exists(t_path) and os.path.exists(value_path):
                t_data = np.load(t_path)
                value_data = np.load(value_path)
                
                if log_type not in data:
                    data[log_type] = {}
                
                data[log_type]['t'] = t_data
                data[log_type]['value'] = value_data
                data[log_type]['columns'] = columns
        
        return data
    def organize_data_to_dataframe(data):
        dfs = []
        
        for log_type, log_data in data.items():
            df = pd.DataFrame(log_data['value'], columns=log_data['columns'])
            df['timestamp'] = log_data['t']
            df.set_index('timestamp', inplace=True)
            dfs.append(df)
        
        # Merge all dataframes on the 'timestamp' column
        merged_df = pd.concat(dfs)
        merged_df.sort_values(by='timestamp', inplace=True)
        merged_df.interpolate(method='linear', inplace=True, limit_direction='both')
        merged_df.reset_index(inplace=True)
        
        return merged_df
    final_data=[]
    for i in os.listdir(SELFDRIVING_IOT_FOLDER+'Chunk_1'):
        for j in os.listdir(SELFDRIVING_IOT_FOLDER+'Chunk_1/'+i):
            data=read_processed_log(SELFDRIVING_IOT_FOLDER+'Chunk_1/'+i+'/'+j)
            combined_df=organize_data_to_dataframe(data)
            final_data.append(combined_df)
    selfdriving_iot=pd.concat(final_data)
    selfdriving_iot.to_csv(OUTPUT_FOLDER+'Selfdriving_IOT_1.csv',index=False)
    final_data=[]
    for i in os.listdir(SELFDRIVING_IOT_FOLDER+'Chunk_2'):
        for j in os.listdir(SELFDRIVING_IOT_FOLDER+'Chunk_2/'+i):
            data=read_processed_log(SELFDRIVING_IOT_FOLDER+'Chunk_2/'+i+'/'+j)
            combined_df=organize_data_to_dataframe(data)
            final_data.append(combined_df)
    selfdriving_iot=pd.concat(final_data)
    selfdriving_iot.to_csv(OUTPUT_FOLDER+'Selfdriving_IOT_2.csv',index=False)
    # Combine the two parts of selfdriving_iot data and delete the original files
    selfdriving_iot_combined = pd.concat([pd.read_csv(OUTPUT_FOLDER+'Selfdriving_IOT_1.csv'), pd.read_csv(OUTPUT_FOLDER+'Selfdriving_IOT_2.csv')])
    selfdriving_iot_combined.to_csv(OUTPUT_FOLDER+'Selfdriving_IOT.csv', index=False)

    # Remove the original files
    os.remove(OUTPUT_FOLDER+'Selfdriving_IOT_1.csv')
    os.remove(OUTPUT_FOLDER+'Selfdriving_IOT_2.csv')
    
def Insurance_claims_data_process():
    """
    Processes insurance claims data by performing the following steps:
    1. Reads the insurance claims data from a CSV file.
    2. Drops rows and columns that are entirely NaN.
    3. Saves the cleaned data to a new CSV file.

    The input file is expected to be located in the directory specified by the 
    `INSUANRANE_CLAIMS_FOLDER` variable and named 'insurance_claims.csv'.
    The output file will be saved in the directory specified by the `OUTPUT_FOLDER` 
    variable and named 'Insurance_Claims.csv'.

    Note:
    - The input CSV file is read with the encoding 'ISO-8859-1'.
    - The output CSV file does not include the index.

    Raises:
    - FileNotFoundError: If the input file does not exist.
    - IOError: If there are issues reading from or writing to the file system.
    """
    insurance_claims=pd.read_csv(INSUANRANE_CLAIMS_FOLDER+'insurance_claims.csv',encoding='ISO-8859-1')
    insurance_claims.dropna(how='all',axis=0,inplace=True)
    insurance_claims.dropna(how='all',axis=1,inplace=True)
    insurance_claims.to_csv(OUTPUT_FOLDER+'Insurance_Claims.csv',index=False)

def main():
    AV_road_test_data_process()
    Selfdriving_crash_data_process()
    Human_driver_behavior_data_process()
    Polidriving_data_process()
    Selfdriving_IOT_data_process()
    Insurance_claims_data_process()

if __name__ == '__main__':
    main()
