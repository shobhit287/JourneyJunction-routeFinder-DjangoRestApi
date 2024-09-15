import os
from dotenv import load_dotenv
from .emailTemplateConfig import emailTemplateConfigs
from .sendEmail import sendEmailNotification
load_dotenv()
def passwordResetSendNotification(data):
    dynamicData= {"userName" : f"{data['first_name']} {data['last_name']}","email":data['email'], "link" : f"{os.getenv('BASE_URL')}?token={data['token']}", "subject": 'Password Reset Request'}
    response = sendEmailNotification(dynamicData, emailTemplateConfigs['PASSWORD_RESET_TEMPLATE'])
    if response['status']:
        print(f"password reset email send successfully to {dynamicData['email']}")
        return {'message': 'Reset link sent to your mail', "status": True}
    else: 
        return response
    
 


    
