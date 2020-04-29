import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore 
from firebase_admin import db 
import json
from firebase import firebase
#**************** ADD DATA TO THE DATABAE ***************
''' NOTE: THIS WILL BE A DIFFERENT DOCUMENT '''
def addDataBase(action, status):
    doc_ref = db.reference(url='https://mobile-iot-58f29.firebaseio.com/MobleIoT/Results') # THE URL TO THE DATABASE WE WANT TO SET
    doc_ref.set({
        u'Action Name':  action,
        u'Status': status
    })

#**************** GET/READ DATA FROM THE DATABASE ************
''' NOTE: WE WANT TO GET THE DATA IN REAL TIME '''
''' NOTE: WE WANT TO READ DATA FROM SPECIFC DOCUMENT '''
''' NOTE: THIS IS THE CALL BACK FUNCTION  FOR 'firebase_admin.db.reference().listen()' '''
def queryDataBase(snapshot): #add 'event' as a parameter
	ref = db.reference(url='https://mobile-iot-58f29.firebaseio.com/MobleIoT/Actions')
	try:
		action = ref.get()
		print(snapshot.val())
		#print(ref.get())
		print("\n")
		print("Got the data")
	except:
		pass
	''' CALL SWITCHER WHICH WHILL CALL THE FUNCTION THAT IS TO DO THE SPECIFIC ACTION '''
	switchAction(action)
def switchAction(action):
	if action == "Erastus desk on":
		erastusDeskon(action)
	elif action == "Erastus desk off":
		erastusDeskOff(action) 
	elif action == "Chris desk on":
		chrisDeskOn(action)
	elif action == "Chris desk off":
		chrisDeskOn(action)
	elif action == "Lamp on":
		lampOn(action)
	elif action == "Lamp off": 
		lampOff(action)
	elif action == "Coffee Maker on": 
		coffeeMakerOn(action)
	elif action == "Coffee Maker off": 
		coffeeMakerOff(action)
	elif action == "Turn ON LED":
		turnOnLED()
	else: 
		unrecAction(action)

#*************** ERASTUS DESK ON FUNCTION *********************
def erastuDeskOn(action):
    ''' NOTE: THIS FUNCTION WILL TURN ON ERASTUS DEASK AND SEND THE STATUS OF IT TO THE DATABASE '''
    print(f"{action}") # this will print the action
    # after turn on the light update the result document
    addDataBase(action, "Erastus Desk on ")
#****************** UNRECOGNIZE ACTION FUCTION ************************
def unrecAction(action):
	result = 'UNRECOGNIZE ACTION'
	print(action)
	addDataBase(action, result)
	
#************** MAIN PYTHON FUCNTION *************************
def main(): 
	#************** SET UP FIREBASE DATABASE ****************
	#cred = credentials.ApplicationDefault() # use auth key if this doesn't work
	cred = credentials.Certificate('mobile-iot-58f29-firebase-adminsdk-tea3m-e82b1617ed.json')

	#firebase_admin.initialize_app(cred, {'databaseURL': 'https://mobile-iot-58f29.firebaseio.com' })
	ref = Firebase.firebaseApplication('https://mobile-iot-58f29.firebaseio.com/', None)
	getRest = ref.get('/Moble/Actios/',None)
	print(getRest)
	#ref = db.reference('MobleIoT/Actions')
	print(ref.get()) # allows me to get data from the data base and print it

	# Will need to call the get functio queryDatabase function here
	
	''' NOTE: A callback functions is called when a data change is detected *** querryDataBase()*** ''' 
	#firebase_admin.db.reference(url='https://mobile-iot-58f29.firebaseio.com/MobleIoT/Actions').on(queryDataBase)
	''' NOTE: THIS MAY NOT BE NEEDED ANYMORE ''' 
	db = firestore.client() # create a firebase datbse client
if __name__ == "__main__":
    main()
