from datetime import datetime
from medicine.models import SavedMedicines
from twilio.rest import Client
from django.contrib.auth.models import auth,User
from Remedy.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

#Live Update
def medicine_time_alert():

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    usera=User.objects.all()
    time_now = datetime.now().time().strftime("%H:%M")
    userc = SavedMedicines.objects.all()
    for user in userc:       
            try:
                medi_time = user.time.get(id=user.id)
                medi_time = datetime.strptime(str(medi_time), "%H:%M:%S").strftime("%H:%M")
            except SavedMedicines.DoesNotExist:
                medi_time = ''
            if medi_time == time_now:
                message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body='It is time for your medicine {} Dosage:{}'.format(user.medicine_name,user.dosage),
                    to='whatsapp:+91{}'.format(usera.username))
                print(usera.mobile)
                print(message.sid)
            