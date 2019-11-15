from PropertyDict import PropertyDict

class Measurements(PropertyDict):
    def __init__(self, **kwargs):
        super(Measurements, self).__init__(kwargs)

def StandardSize(size):
    s6 = Measurements(size=6, Bust=76, Waist=56, LowWaist=68, Hips=82, BackWidth=31.4, Chest=28.8, Shoulder=11.5, NeckSize=34, Dart=5.2, TopArm=25.5, Wrist=14.5, Ankle=22.5, HighAnkle=19.5, NapeToWaist=39.8, FrontShoulderToWaist=39.8, ArmscyeDepth=19.8, WaistToKnee=57, WaistToHip=19.7, WaistToFloor=101, BodyRise=25.9, SleeveLength=57, SleeveLengthJersey=53)
    s8 = Measurements(size=8, Bust=80, Waist=60, LowWaist=72, Hips=86, BackWidth=32.4, Chest=30, Shoulder=11.75, NeckSize=35, Dart=5.8, TopArm=26.5, Wrist=15, Ankle=23, HighAnkle=20, NapeToWaist=40.2, FrontShoulderToWaist=40.2, ArmscyeDepth=20.2, WaistToKnee=57.5, WaistToHip=20, WaistToFloor=102, BodyRise=26.6, SleeveLength=57.5, SleeveLengthJersey=53.5)
    s10 = Measurements(size=10, Bust=84, Waist=64, LowWaist=76, Hips=90, BackWidth=33.4, Chest=31.2, Shoulder=12, NeckSize=36, Dart=6.4, TopArm=27.5, Wrist=15.5, Ankle=23.5, HighAnkle=20.5, NapeToWaist=40.6, FrontShoulderToWaist=40.6, ArmscyeDepth=20.6, WaistToKnee=58, WaistToHip=20.3, WaistToFloor=103, BodyRise=27.3, SleeveLength=58, SleeveLengthJersey=54)
    s12 = Measurements(size=12, Bust=88, Waist=68, LowWaist=80, Hips=94, BackWidth=34.4, Chest=32.4, Shoulder=12.25, NeckSize=37, Dart=7, TopArm=28.5, Wrist=16, Ankle=24, HighAnkle=21, NapeToWaist=41, FrontShoulderToWaist=41, ArmscyeDepth=21, WaistToKnee=58.5, WaistToHip=20.6, WaistToFloor=104, BodyRise=28, SleeveLength=58.5, SleeveLengthJersey=54.5)
    s14 = Measurements(size=14, Bust=92, Waist=72, LowWaist=84, Hips=98, BackWidth=35.4, Chest=33.6, Shoulder=12.5, NeckSize=38, Dart=7.6, TopArm=29.5, Wrist=16.5, Ankle=24.5, HighAnkle=21.5, NapeToWaist=41.4, FrontShoulderToWaist=41.4, ArmscyeDepth=21.4, WaistToKnee=59, WaistToHip=20.9, WaistToFloor=105, BodyRise=28.7, SleeveLength=59, SleeveLengthJersey=55)
    s16 = Measurements(size=16, Bust=96, Waist=76, LowWaist=88, Hips=102, BackWidth=36.4, Chest=34.8, Shoulder=12.75, NeckSize=39, Dart=8.2, TopArm=30.5, Wrist=17, Ankle=25, HighAnkle=22, NapeToWaist=41.8, FrontShoulderToWaist=41.8, ArmscyeDepth=21.8, WaistToKnee=59.5, WaistToHip=21.2, WaistToFloor=106, BodyRise=29.4, SleeveLength=59.5, SleeveLengthJersey=55.5)

    s = {"6":s6, "8":s8, "10":s10, "12":s12, "14":s14, "16":s16}

    return s[size]