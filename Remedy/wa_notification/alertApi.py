from datetime import datetime
from register_pat.models import PatientRec,MedicineTime
from twilio.rest import Client
from Remedy.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

#Live Update
def medicine_time_alert():

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    time_now = datetime.now().time().strftime("%H:%M")
    patient_rec = PatientRec.objects.all()
    times = MedicineTime.objects.all()
    for record in patient_rec:       
        for time in times:
            try:
                medi_time = record.medicine_time.get(id=time.id)
                medi_time = datetime.strptime(str(medi_time), "%H:%M:%S").strftime("%H:%M")
            except MedicineTime.DoesNotExist:
                medi_time = ''
            if medi_time == time_now:
                message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body='It is time for your medicine {} Dosage:{}'.format(record.medicine_rec.medicine_name,record.dosage),
                    to='whatsapp:+91{}'.format(record.mobile))
                print(record.mobile)
                print(message.sid)
            