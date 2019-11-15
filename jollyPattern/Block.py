from PropertyDict import PropertyDict
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        return Point(self.x * factor, self.y * factor)

class Block:
    def __init__(self, meas):
        self.meas = meas
        self.points = PropertyDict()

    def PointsAsArrays(self):
        name = []
        x = []
        y = []
        for k, v in self.points._dict.items():
            name.append(k)
            x.append(v.x)
            y.append(v.y)
        return name, x, y

class BlockPiece:
    def __init__(self, points, nodeList):
        self.points = points
        self.nodeList = nodeList

    def PointArrays(self, closed=False):
        x = []
        y = []
        for n in self.nodeList.split(","):
            pnt = self.points._dict[n]
            x.append(pnt.x)
            y.append(pnt.y)
        if closed:
            x.append(x[0])
            y.append(y[0])
        return (x, y)

class CloseFittingBodice(Block):
    def __init__(self, meas):
        super(CloseFittingBodice, self).__init__(meas)
        self.meas = meas

        self.points._0 = Point(0, 0)
        # 0–1 1.5 cm.
        self.points._1 = self.points._0 + Point(0, 1.5)
        # 1–2 armscye depth measurement plus 0.5 cm
        self.points._2 = self.points._1 + Point(0, meas.ArmscyeDepth + 0.5)
        # 2–3 half bust plus 5 cm
        cfOffset = Point(meas.Bust/2+5, 0)
        self.points._3 = self.points._2 + cfOffset
        # 3–4 = 0–2
        # When using body sizes from the standard body measurement chart (page 13) or personal measurements (page 178):
        # Add an extra 0.5 cm for each size up above size 14.
        self.points._4 = self.points._0 + cfOffset + (Point(0,0) if meas.size<=14 else Point(0.5, 0)*(meas.size-14))
        # 1–5 nape to waist measurement; square across to 6.
        self.points._5 = self.points._1 + Point(0, meas.NapeToWaist)
        self.points._6 = self.points._5 + cfOffset
        # 5–7 waist to hip measurement; square across to centre front line.
        # Mark point 8 (this gives half hip measurement plus 2.5 cm ease).
        self.points._7 = self.points._5 + Point(0, meas.WaistToHip)
        self.points._8 = self.points._7 + cfOffset

        ### BACK
        # 0–9 one fifth neck size minus 0.2 cm;
        self.points._9 = self.points._0 + Point(meas.NeckSize/5, 0)
        # 1–10 one fifth armscye depth measurement minus 0.7 cm
        self.points._10 = self.points._1 + Point(0, meas.ArmscyeDepth/5 - 0.7)
        # 9–11 shoulder length measurement plus 1 cm
        # draw back shoulder line to touch the line from 10.
        y9_10 = self.points._10.y - self.points._9.y
        self.points._11 = Point(self.points._9.x + math.sqrt(meas.Shoulder*meas.Shoulder - y9_10*y9_10), 
                            self.points._10.y)
        # 12 centre of shoulder line.
        self.points._12 = (self.points._11 + self.points._9) * 0.5
        # 12–13 draw a dotted line 5 cm long and sloping
        # inwards 1 cm. Construct dart 1 cm wide with this line
        # as centre (make both sides of dart the same length).
        self.points._13 = self.points._12 + Point(-1, math.sqrt(5*5-1*1))
        # 2–14 half back width measurement plus 0.5 cm ease; square up to 15.
        self.points._14 = self.points._2 + Point(meas.BackWidth/2 +0.5, 0)
        self.points._15 = Point(self.points._14.x, self.points._10.y)
        # 14–16 half the measurement 14–15.
        self.points._16 = (self.points._14 + self.points._15) * 0.5
        # 17 midway between 2 and 14; square down with a
        # dotted line to point 18 on waistline, and point 19 on the hipline.
        self.points._17 = (self.points._2 + self.points._14) * 0.5
        self.points._18 = Point(self.points._17.x, self.points._5.y)
        self.points._19 = Point(self.points._17.x, self.points._7.y)

        ### FRONT
        # 4–20 one fifth neck size minus 0.7 cm.
        self.points._20 = self.points._4 + Point(-meas.NeckSize/5 - 0.7, 0)
        # 4–21 one fifth neck size minus 0.2 cm; draw in front neck curve 20–21.
        self.points._21 = self.points._4 + Point(0, meas.NeckSize/5 - 0.2)
        # 3–22 half chest measurement plus half width of dart
        self.points._22 = self.points._3 - Point((meas.Chest + meas.Dart)/2, 0)
        # 3–23 half the measurement 3–22; square down with
        # a dotted line to point 24 on waistline and 25 on hipline
        self.points._23 = (self.points._3 + self.points._22) * 0.5
        self.points._24 = Point(self.points._23.x, self.points._5.y)
        self.points._25 = Point(self.points._23.x, self.points._7.y)
        # 26 is the bust point 2.5 cm down from 23;
        self.points._26 = self.points._23 + Point(0, 2.5)
        # 20–27 dart width measurement
        self.points._27 = self.points._20 - Point(meas.Dart, 0)
        # 11–28 1.5 cm; square out approx. 10 cm to 29.
        self.points._28 = self.points._11 + Point(0, 1.5)
        self.points._29 = self.points._28 + Point(10, 0)
        # 27–30 draw a line from 27, shoulder length measurement, to touch the line from 28–29.
        y27_28 = self.points._28.y - self.points._27.y
        self.points._30 = Point(self.points._27.x - math.sqrt(meas.Shoulder*meas.Shoulder - y27_28*y27_28), 
                            self.points._28.y)
        # 22–31 one third the measurement 3–21.
        self.points._31 = self.points._22 - Point(0, (self.points._3.y - self.points._21.y)/3)
        # 32 is midway between 14 and 22; square down with a dotted line to point 33 on the waistline
        # and point 34 on the hipline.
        self.points._32 = (self.points._14 + self.points._22) * 0.5
        self.points._33 = Point(self.points._32.x, self.points._5.y)
        self.points._34 = Point(self.points._32.x, self.points._7.y)

    def Pieces(self):
        return [BlockPiece(self.points, "_1,_10,_2,_5,_7,_8,_6,_3,_21,_20,_26,_27,_30,_31,_32,_16,_11,_12,_13,_12,_9")]

if __name__=="__main__":
    import trash