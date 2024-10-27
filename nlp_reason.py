import pandas as pd
import openai
import logging
path='dataset/data/'
logging.basicConfig(level=logging.INFO)
def get_data(path):
    avtest = pd.read_csv(path+'AVTEST_Disengagements.csv')
    avtest=avtest['DESCRIPTION OF FACTS CAUSING DISENGAGEMENT'].astype('str').tolist()
    selfdriving_crash=pd.read_csv(path+'Selfdriving_Crash.csv')
    selfdriving_crash=selfdriving_crash['Narrative'].astype('str').tolist()
    return avtest,selfdriving_crash

def openai_server():
    api_key = "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"
    return openai.OpenAI(api_key=api_key).chat.completions

def get_chat_response(chat_response,chat_input,type,batch_size):
    if type=='avtest':
        response = chat_response.create(
            model="gpt-4o",
            messages=[
            {"role": "system", "content": f"You need to categorize these reasons of disengagements. The categories include Software Issues, Hardware Problems, Environmental Factors, Human Factors, System Limitations, and Regulatory Compliance. The input is sepearted by $ for each reason. You only need to output the categories seperated by comma. The output should be in the same order as the input with size {batch_size}."},
            {"role": "user", "content": chat_input},
            ],
        )
        return response.choices[0].message.content
    elif type=='selfdriving_crash':
        response = chat_response.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You need to categorize these reasons of disengagements. The categories include Perception Failures, Decision-Making Errors, Control System Failures, Sensor and Hardware Malfunctions, Environmental Hazards, Human Factors, and External Factors. The input is sepearted by $ for each reason. You only need to output the categories seperated by comma. The output should be in the same order as the input with size {batch_size}."},
                {"role": "user", "content": chat_input},
            ],
        )
        return response.choices[0].message.content
def categorize_data(path):
    avtest, selfdriving_crash = get_data(path)
    chat_response = openai_server()
    batch_size = 100
    selfdriving_crash_categories = []
    avtest_categories = []
    for i in range(0, len(avtest), batch_size):
        batch = list(avtest)[i:i + batch_size]
        response = get_chat_response(chat_response, "$".join(batch), 'avtest',batch_size)
        response=response.split(',')
        if len(response)>batch_size:
            response=response[:batch_size]
        elif len(response)<=batch_size:
            response.extend(['']*(batch_size-len(response)))
        if i+batch_size>len(avtest):
            response=response[:len(avtest)-i]
        avtest_categories.extend(response)
        logging.info(f"Batch {i} completed: avtest-{len(response)}")
    for i in range(0, len(selfdriving_crash), batch_size):
        batch = list(selfdriving_crash)[i:i + batch_size]
        response = get_chat_response(chat_response, "$".join(batch), 'selfdriving_crash',batch_size)
        response=response.split(',')
        if len(response)>batch_size:
            response=response[:batch_size]
        elif len(response)<=batch_size:
            response.extend(['']*(batch_size-len(response)))
        if i+batch_size>len(selfdriving_crash):
            response=response[:len(selfdriving_crash)-i]
        selfdriving_crash_categories.extend(response)
        logging.info(f"Batch {i} completed: selfdriving_crash-{len(response)}")
    
    return avtest_categories, selfdriving_crash_categories
def output_category(avtest_categories, selfdriving_crash_categories):
    avtest = pd.read_csv(path+'AVTEST_Disengagements.csv')
    selfdriving_crash = pd.read_csv(path+'Selfdriving_Crash.csv')
    # Ensure the length of categories matches the length of the dataframe
    avtest['categories'] = avtest_categories
    avtest.to_csv(path+'AVTEST_Disengagements.csv')
    selfdriving_crash['categories'] = selfdriving_crash_categories
    selfdriving_crash.to_csv(path+'Selfdriving_Crash.csv')

if __name__ == '__main__':
    avtest_categories, selfdriving_crash_categories = categorize_data(path)
    logging.info(avtest_categories)
    logging.info(len(avtest_categories))
    logging.info(selfdriving_crash_categories)
    logging.info(len(selfdriving_crash_categories))
    output_category(avtest_categories, selfdriving_crash_categories)