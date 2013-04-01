'''
Created on 2013. 3. 27.

@author: stmkmk
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *


MAGIC_NUMBER = 0x570C4
FILE_VERSION = 1


class Ship(object):
    def __init__(self, name, owner, country, teu=0, description=""):
        self.name = QString(name)
        self.owner = QString(owner)
        self.country = QString(country)
        self.teu = teu
        self.description = QString(description)
    
class ShipContainer(object):
    
    def __init__(self,filename=QString()):
        self.filename = QString(filename)
        self.dirty = False
        self.ships = {}
        self.owners = set()
        self.countries = set()
    
    def __len__(self):
        return len(self.ships)
    
    def __iter__(self):
        for ship in self.ships.values():
            yield ship 
        
    def ship(self,identity):
        return self.ships.get(identity)
    
    def addShip(self,ship):
        self.ships[id(ship)] = ship
        self.owners.add(ship.owner)
        self.countries.add(ship.country)
        self.dirty = True
        
    def removeShip(self, ship):
        del self.ships[id(ship)]
        del ship
        self.dirty = True
        
    def inOrder(self):
        return sorted(self.ships.values())
    
    def inCountryOwnerOrder(self):
        return sorted(self.ships.values(), key = lambda x:(x.country, x.owner, x.name))
    
    def load(self):
        fh = None
        
        if self.filename.isEmpty():
            raise IOError("no file name")
        fh = QFile(self.filename)
        
        if not fh.open(QIODevice.ReadOnly):
            raise IOError(str(fh.errorString()))
        
        stream = QDataStream(fh)
        magic = stream.readInt32()
        
        if magic != MAGIC_NUMBER:
            raise IOError("unrecognized file type")
        
        fileversion = stream.readint16()
        if fileversion != FILE_VERSION:
            raise IOError("unrecognized file type version")
        
        self.ships = {}
        
        while not fh.atEnd():
            name = QString()
            country = QString()
            owner = QString()
            description = QString()
            stream >> name >> owner >> country >> description
            teu = stream.readInt32()
            
            ship = Ship(name, owner, country, teu, description)
            self.ships[id(ship)] = ship
            self.owners.add[str(owner)]
            self.countries.add[str(country)]
        
        self.dirty = False
        fh.close()

    def save(self):
        fh = None
        if self.filename is None:
            raise IOError("no file name for saving")
        fh = QFile(self.filename)
        
        if not fh.open(QIODevice.WriteOnly):
            raise IOError(str(fh.errorString()))
        
        stream = QDataStream(fh)
        stream.writeInt32(MAGIC_NUMBER)
        stream.writeInt16(FILE_VERSION)
        
        for ship in self.ships.values():
            stream << ship.name << ship.owenr << ship.country << ship.description
            stream.writeInt32(ship.teu)
        self.dirty = False
        
        fh.close()
        
        
    def generateFakeShips(self):
        for name, owner, country, teu, description in (
    ("Emma M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 151687,
     "<b>W\u00E4rtsil\u00E4-Sulzer RTA96-C</b> main engine,"
     "<font color=green>109,000 hp</font>"),
    ("MSC Pamela", "MSC", "Liberia", 90449,
     "Draft <font color=green>15m</font>"),
    ("Colombo Express", "Hapag-Lloyd", "Germany", 93750,
     "Main engine, <font color=green>93,500 hp</font>"),
    ("Houston Express", "Norddeutsche Reederei", "Germany", 95000,
     "Features a <u>twisted leading edge full spade rudder</u>. "
     "Sister of <i>Savannah Express</i>"),
    ("Savannah Express", "Norddeutsche Reederei", "Germany", 95000,
     "Sister of <i>Houston Express</i>"),
    ("MSC Susanna", "MSC", "Liberia", 90449, ""),
    ("Eleonora M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 151687,
     "Captain <i>Hallam</i>"),
    ("Estelle M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 151687,
     "Captain <i>Wells</i>"),
    ("Evelyn M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 151687,
      "Captain <i>Byrne</i>"),
    ("Georg M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
    ("Gerd M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
    ("Gjertrud M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
    ("Grete M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
    ("Gudrun M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
    ("Gunvor M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
    ("CSCL Le Havre", "Danaos Shipping", "Cyprus", 107200, ""),
    ("CSCL Pusan", "Danaos Shipping", "Cyprus", 107200,
     "Captain <i>Watts</i>"),
    ("Xin Los Angeles", "China Shipping Container Lines (CSCL)",
     "Hong Kong", 107200, ""),
    ("Xin Shanghai", "China Shipping Container Lines (CSCL)", "Hong Kong",
     107200, ""),
    ("Cosco Beijing", "Costamare Shipping", "Greece", 99833, ""),
    ("Cosco Hellas", "Costamare Shipping", "Greece", 99833, ""),
    ("Cosco Guangzho", "Costamare Shipping", "Greece", 99833, ""),
    ("Cosco Ningbo", "Costamare Shipping", "Greece", 99833, ""),
    ("Cosco Yantian", "Costamare Shipping", "Greece", 99833, ""),
    ("CMA CGM Fidelio", "CMA CGM", "France", 99500, ""),
    ("CMA CGM Medea", "CMA CGM", "France", 95000, ""),
    ("CMA CGM Norma", "CMA CGM", "Bahamas", 95000, ""),
    ("CMA CGM Rigoletto", "CMA CGM", "France", 99500, ""),
    ("Arnold M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496,
     "Captain <i>Morrell</i>"),
    ("Anna M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496,
     "Captain <i>Lockhart</i>"),
    ("Albert M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496,
     "Captain <i>Tallow</i>"),
    ("Adrian M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496,
     "Captain <i>G. E. Ericson</i>"),
    ("Arthur M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496, ""),
    ("Axel M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496, ""),
    ("NYK Vega", "Nippon Yusen Kaisha", "Panama", 97825, ""),
    ("MSC Esthi", "MSC", "Liberia", 99500, ""),
    ("MSC Chicago", "Offen Claus-Peter", "Liberia", 90449, ""),
    ("MSC Bruxelles", "Offen Claus-Peter", "Liberia", 90449, ""),
    ("MSC Roma", "Offen Claus-Peter", "Liberia", 99500, ""),
    ("MSC Madeleine", "MSC", "Liberia", 107551, ""),
    ("MSC Ines", "MSC", "Liberia", 107551, ""),
    ("Hannover Bridge", "Kawasaki Kisen Kaisha", "Japan", 99500, ""),
    ("Charlotte M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Clementine M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Columbine M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Cornelia M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Chicago Express", "Hapag-Lloyd", "Germany", 93750, ""),
    ("Kyoto Express", "Hapag-Lloyd", "Germany", 93750, ""),
    ("Clifford M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Sally M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Sine M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Skagen M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Sofie M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Sor\u00F8 M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Sovereing M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Susan M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Svend M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Svendborg M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("A.P. M\u00F8ller", "M\u00E6rsk Line", "Denmark", 91690,
     "Captain <i>Ferraby</i>"),
    ("Caroline M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Carsten M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Chastine M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("Cornelius M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
    ("CMA CGM Otello", "CMA CGM", "France", 91400, ""),
    ("CMA CGM Tosca", "CMA CGM", "France", 91400, ""),
    ("CMA CGM Nabucco", "CMA CGM", "France", 91400, ""),
    ("CMA CGM La Traviata", "CMA CGM", "France", 91400, ""),
    ("CSCL Europe", "Danaos Shipping", "Cyprus", 90645, ""),
    ("CSCL Africa", "Seaspan Container Line", "Cyprus", 90645, ""),
    ("CSCL America", "Danaos Shipping ", "Cyprus", 90645, ""),
    ("CSCL Asia", "Seaspan Container Line", "Hong Kong", 90645, ""),
    ("CSCL Oceania", "Seaspan Container Line", "Hong Kong", 90645,
     "Captain <i>Baker</i>"),
    ("M\u00E6rsk Seville", "Blue Star GmbH", "Liberia", 94724, ""),
    ("M\u00E6rsk Santana", "Blue Star GmbH", "Liberia", 94724, ""),
    ("M\u00E6rsk Sheerness", "Blue Star GmbH", "Liberia", 94724, ""),
    ("M\u00E6rsk Sarnia", "Blue Star GmbH", "Liberia", 94724, ""),
    ("M\u00E6rsk Sydney", "Blue Star GmbH", "Liberia", 94724, ""),
    ("MSC Heidi", "MSC", "Panama", 95000, ""),
    ("MSC Rania", "MSC", "Panama", 95000, ""),
    ("MSC Silvana", "MSC", "Panama", 95000, ""),
    ("M\u00E6rsk Stralsund", "Blue Star GmbH", "Liberia", 95000, ""),
    ("M\u00E6rsk Saigon", "Blue Star GmbH", "Liberia", 95000, ""),
    ("M\u00E6rsk Seoul", "Blue Star Ship Managment GmbH", "Germany",
     95000, ""),
    ("M\u00E6rsk Surabaya", "Offen Claus-Peter", "Germany", 98400, ""),
    ("CMA CGM Hugo", "NSB Niederelbe", "Germany", 90745, ""),
    ("CMA CGM Vivaldi", "CMA CGM", "Bahamas", 90745, ""),
    ("MSC Rachele", "NSB Niederelbe", "Germany", 90745, ""),
    ("Pacific Link", "NSB Niederelbe", "Germany", 90745, ""),
    ("CMA CGM Carmen", "E R Schiffahrt", "Liberia", 89800, ""),
    ("CMA CGM Don Carlos", "E R Schiffahrt", "Liberia", 89800, ""),
    ("CMA CGM Don Giovanni", "E R Schiffahrt", "Liberia", 89800, ""),
    ("CMA CGM Parsifal", "E R Schiffahrt", "Liberia", 89800, ""),
    ("Cosco China", "E R Schiffahrt", "Liberia", 91649, ""),
    ("Cosco Germany", "E R Schiffahrt", "Liberia", 89800, ""),
    ("Cosco Napoli", "E R Schiffahrt", "Liberia", 89800, ""),
    ("YM Unison", "Yang Ming Line", "Taiwan", 88600, ""),
    ("YM Utmost", "Yang Ming Line", "Taiwan", 88600, ""),
    ("MSC Lucy", "MSC", "Panama", 89954, ""),
    ("MSC Maeva", "MSC", "Panama", 89954, ""),
    ("MSC Rita", "MSC", "Panama", 89954, ""),
    ("MSC Busan", "Offen Claus-Peter", "Panama", 89954, ""),
    ("MSC Beijing", "Offen Claus-Peter", "Panama", 89954, ""),
    ("MSC Toronto", "Offen Claus-Peter", "Panama", 89954, ""),
    ("MSC Charleston", "Offen Claus-Peter", "Panama", 89954, ""),
    ("MSC Vittoria", "MSC", "Panama", 89954, ""),
    ("Ever Champion", "NSB Niederelbe", "Marshall Islands", 90449,
     "Captain <i>Phillips</i>"),
    ("Ever Charming", "NSB Niederelbe", "Marshall Islands", 90449,
     "Captain <i>Tonbridge</i>"),
    ("Ever Chivalry", "NSB Niederelbe", "Marshall Islands", 90449, ""),
    ("Ever Conquest", "NSB Niederelbe", "Marshall Islands", 90449, ""),
    ("Ital Contessa", "NSB Niederelbe", "Marshall Islands", 90449, ""),
    ("Lt Cortesia", "NSB Niederelbe", "Marshall Islands", 90449, ""),
    ("OOCL Asia", "OOCL", "Hong Kong", 89097, ""),
    ("OOCL Atlanta", "OOCL", "Hong Kong", 89000, ""),
    ("OOCL Europe", "OOCL", "Hong Kong", 89097, ""),
    ("OOCL Hamburg", "OOCL", "Marshall Islands", 89097, ""),
    ("OOCL Long Beach", "OOCL", "Marshall Islands", 89097, ""),
    ("OOCL Ningbo", "OOCL", "Marshall Islands", 89097, ""),
    ("OOCL Shenzhen", "OOCL", "Hong Kong", 89097, ""),
    ("OOCL Tianjin", "OOCL", "Marshall Islands", 89097, ""),
    ("OOCL Tokyo", "OOCL", "Hong Kong", 89097, "")):
            yield Ship(name, owner, country, teu, description)            
            
            