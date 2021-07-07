#!/usr/bin/env python3

import serial
import time
import paho.mqtt.client as paho
import json

class AVR:
    def __init__(self, port):
        self.port = port
        self.from_dB = { '-80': '00',
			 '-79.5': '005',
			 '-79': '01',
			 '-78.5': '015',
			 '-78': '02',
			 '-77.5': '025',
			 '-77': '03',
			 '-76.5': '035',
			 '-76': '04',
			 '-75.5': '045',
			 '-75': '05',
			 '-74.5': '055',
			 '-74': '06',
			 '-73.5': '065',
			 '-73': '07',
			 '-72.5': '075',
			 '-72': '08',
			 '-71.5': '085',
			 '-71': '09',
			 '-70.5': '095',
			 '-70': '10',
			 '-69.5': '105',
			 '-69': '11',
			 '-68.5': '115',
			 '-68': '12',
			 '-67.5': '125',
			 '-67': '13',
			 '-66.5': '135',
			 '-66': '14',
			 '-65.5': '145',
			 '-65': '735',
			 '-64.5': '155',
			 '-64': '16',
			 '-63.5': '165',
			 '-63': '17',
			 '-62.5': '175',
			 '-62': '18',
			 '-61.5': '185',
			 '-61': '19',
			 '-60.5': '195',
			 '-60': '20',
			 '-59.5': '205',
			 '-59': '21',
			 '-58.5': '215',
			 '-58': '22',
			 '-57.5': '225',
			 '-57': '23',
			 '-56.5': '235',
			 '-56': '24',
			 '-55.5': '245',
			 '-55': '25',
			 '-54.5': '255',
			 '-54': '26',
			 '-53.5': '265',
			 '-53': '27',
			 '-52.5': '275',
			 '-52': '28',
			 '-51.5': '285',
			 '-51': '29',
			 '-50.5': '295',
			 '-50': '30',
			 '-49.5': '305',
			 '-49': '31',
			 '-48.5': '315',
			 '-48': '32',
			 '-47.5': '325',
			 '-47': '33',
			 '-46.5': '335',
			 '-46': '34',
			 '-45.5': '345',
			 '-45': '35',
			 '-44.5': '355',
			 '-44': '36',
			 '-43.5': '365',
			 '-43': '37',
			 '-42.5': '375',
			 '-42': '38',
			 '-41.5': '385',
			 '-41': '39',
			 '-40.5': '395',
			 '-40': '40',
			 '-39.5': '405',
			 '-39': '41',
			 '-38.5': '415',
			 '-38': '42',
			 '-37.5': '425',
			 '-37': '43',
			 '-36.5': '435',
			 '-36': '44',
			 '-35.5': '445',
			 '-35': '45',
			 '-34.5': '455',
			 '-34': '46',
			 '-33.5': '465',
			 '-33': '47',
			 '-32.5': '475',
			 '-32': '48',
			 '-31.5': '485',
			 '-31': '49',
			 '-30.5': '495',
			 '-30': '50',
			 '-29.5': '505',
			 '-29': '51',
			 '-28.5': '515',
			 '-28': '52',
			 '-27.5': '525',
			 '-27': '53',
			 '-26.5': '535',
			 '-26': '54',
			 '-25.5': '545',
			 '-25': '55',
			 '-24.5': '555',
			 '-24': '56',
			 '-23.5': '565',
			 '-23': '57',
			 '-22.5': '575',
			 '-22': '58',
			 '-21.5': '585',
			 '-21': '59',
			 '-20.5': '595',
			 '-20': '60',
			 '-19.5': '605',
			 '-19': '61',
			 '-18.5': '615',
			 '-18': '62',
			 '-17.5': '625',
			 '-17': '63',
			 '-16.5': '635',
			 '-16': '64',
			 '-15.5': '645',
			 '-15': '65',
			 '-14.5': '655',
			 '-14': '66',
			 '-13.5': '665',
			 '-13': '67',
			 '-12.5': '675',
			 '-12': '68',
			 '-11.5': '685',
			 '-11': '69',
			 '-10.5': '695',
			 '-10': '70',
			 '-9.5': '705',
			 '-9': '71',
			 '-8.5': '715',
			 '-8': '72',
                         '-7.5':'725',
			 '-7': '73',
			 '-7.': '735',
			 '-6': '74',
			 '-6.5': '745',
			 '-5': '75',
			 '-5.5': '755',
			 '-4': '76',
			 '-4.5': '765',
			 '-3': '77',
			 '-3.5': '775',
			 '-2': '78',
			 '-2.5': '785',
			 '-1': '79',
			 '-0.5': '795 ',
			 '0': '80',
			 '0.5': '805 ',
			 '1': '81',
			 '1.5': '95',
			 '2': '82',
			 '2.5': '825 ',
			 '3': '83',
			 '3.5': '835 ',
			 '4': '84',
			 '4.5': '845 ',
			 '5': '85',
			 '5.5': '855 ',
			 '6': '86',
			 '6.5': '865 ',
			 '7': '87',
			 '7.5': '875 ',
			 '8': '88',
			 '8.5': '885 ',
			 '9': '89',
			 '9.5': '895',
			 '10': '90',
			 '10.5': '905',
			 '11': '91',
			 '11.5': '915',
			 '12': '92',
			 '12.5': '925',
			 '13': '93',
			 '13.5': '935',
			 '14': '94',
			 '14.5': '945',
                         '15': '95',
			 '15,5': '955',
			 '16': '96',
			 '16.5': '965',
			 '17': '97',
			 '17.5': '975',
			 '18': '98',
			 '--': '99'}

        self.to_dB = {v: k for k, v in self.from_dB.items()}
        self.state = {
                'power' : 'unknown',
                'master_volume' : 00,
                'master_volume_db' : -80,
                'master_volume_max' : 00,
                'master_volume_max_db': -80,
                'mute' : 'unknown',
                'input' : 'unknown'
                }

    def connect(self):
        # Set up serial port
        self.ser = serial.Serial(
            self.port,\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS)

        # Flush read and write buffer
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

        # Get current state from reciver
        self.get_state()


    def get_state(self):
        # Get power state
        # Returns both power state and SSHDP
        self.write("PW?")
        self.decode(self.read())
        self.decode(self.read())
        time.sleep(0.05)

        # Get volume
        # Returns both max volume and main volume
        self.write("MV?")
        self.decode(self.read())
        self.decode(self.read())
        time.sleep(0.05)

        # Get mute
        self.write("MU?")
        self.decode(self.read())
        time.sleep(0.05)

        # Get input
        self.write("SI?")
        self.decode(self.read())
        time.sleep(0.05)

    def disconnect(self):
        self.ser.close()

    def read(self):
        return self.ser.read_until(b'\r').strip().decode('ascii')

    def write(self, cmd):
        cmd = cmd + '\r'
        return self.ser.write(cmd.encode('utf-8'))

    def to_float(self, value):
        if len(value) == 3:
            return float(value[0:2] + '.' + value[2:3])
        else:
            return float(value)

    def decode(self, line):
        """ Asume all commands start with only two chars, do cleanup in function """
        method_name = str(line[:2])
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda a : print("Unsupported command: " + line))
        # Call the method as we return it
        return method(line[2:])

    def MV(self, volume):
        if "MAX " in volume:
            try:
                self.state['master_volume_max_db'] = float(self.to_dB[volume[4:]])
                self.state['master_volume_max'] = self.to_float(volume[4:])
                return True
            except:
                return False

        try:
            self.state['master_volume_db'] = float(self.to_dB[volume])
            self.state['master_volume'] = self.to_float(volume)
            return True
        except:
            return False

    def PW(self, state):
        self.state['power'] = state
        return True

    def MU(self, state):
        self.state['mute'] = state
        return True

    def SI(self, state):
        self.state['input'] = state
        return True

class MQTT:
    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.client = paho.Client("AVRMQTT")

    def connect(self):
        self.client.connect(self.broker)
        self.client.loop_start()

    def publish(self, message):
        self.client.publish(self.topic, message)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()


print("Init AVR")
avr = AVR('/dev/avr2808')
print("Connecting")
avr.connect()
print("connected to: " + avr.port)

debug=False
print("Init MQTT")
mqtt = MQTT("127.0.0.1", "AVR")
mqtt.connect()
mqtt.publish(json.dumps(avr.state))

print("Listening on serial port")
while True:
    line = ''
    line = avr.read()
    output = avr.decode(line)

    if (debug):
        print(json.dumps(avr.state))

    if (output):
        mqtt.publish(json.dumps(avr.state))

print("Disconnecting")
avr.disconnect()
mqtt.disconnect()
