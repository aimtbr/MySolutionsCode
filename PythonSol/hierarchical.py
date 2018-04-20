import threading, sys, os
import xml.etree.ElementTree as et
from pathlib import Path


class Ambulance:
    def __init__(self):
        self.ambulance_brigades = {}
        self.functions_ambulance = {"1. Create new brigade": self.new_brigade,
                                    "2. Open brigade": self.open_brigade,
                                    "3. Delete brigade": self.delete_brigade,
                                    "0. Exit": sys.exit}
        self.ambulance_number = ""
        self.db_directory = "C:\\Users\\User\\Desktop\\database.xml"        #Path to save the database data
        self.check_file()

    def check_file(self):
        path = Path(self.db_directory)
        if path.exists() is False:
            crt_path = open(self.db_directory, "w")
            crt_path.close()
        if os.stat(self.db_directory).st_size == 0:
            ambulance = et.Element("ambulance")
            amb_number = et.SubElement(ambulance, "amb_number")
            amb_number.text = "Ambulance number: " + input("Ambulance number: ")
            with open(self.db_directory, "wb") as wr:
                wr.write(et.tostring(ambulance))
        self.tree = et.parse(self.db_directory)
        self.tree_root = self.tree.getroot()

    def start_ambulance_control(self):
        def ambulance_control():
            self.checker = True
            while self.checker:
                for each in list(self.functions_ambulance.keys()):
                    print(each)
                inp = input("What to do: ")
                for each in list(self.functions_ambulance.keys()):
                    if inp == each[:each.index(".")]:
                        self.functions_ambulance[each]()
                        break
                else:
                    print("Invalid input.")
        thr = threading.Thread(target=ambulance_control)
        thr.start()

    def delete_brigade(self):
        if len(self.ambulance_brigades.keys()) != 0:
            print("Available brigades: " + ", ".join(
                [x.lstrip("Brigade number: ") for x in list(self.ambulance_brigades.keys())]))
            inp = input("Enter the number of brigade to delete: ")
            if inp != "0":
                if inp in [x.lstrip("Brigade number: ") for x in list(self.ambulance_brigades.keys())]:
                    self.ambulance_brigades.pop("Brigade number: {}".format(inp))
                    self.tree_root.remove(self.tree_root.find("brigade_{}".format(inp)))
                    self.tree.write(self.db_directory)
                else:
                    print("There is no such brigade.")
        else:
            print("There is not a single brigade.")

    def open_brigade(self):
        if len(self.ambulance_brigades.keys()) != 0:
            print("Available brigades: " + ", ".join(
                [x.lstrip("Brigade number: ") for x in list(self.ambulance_brigades.keys())]))
            inp = input("Enter brigade number: ")
            for each in list(self.ambulance_brigades.keys()):
                if inp == each.lstrip("Brigade number: "):
                    self.checker = False
                    self.ambulance_brigades[each].start_brigade_control()
                    break
            else:
                print("There is no such brigade.")
        else:
            print("There is not a simple brigade.")

    def new_brigade(self):
        br_num = "Brigade number: " + input("Brigade number: ")
        if br_num not in list(self.ambulance_brigades.keys()):
            c_num = "Coach number: " + input("Coach number: ")
            driver_fn = "Full name of the driver: " + input("Full name of the driver: ")
            corpsman_fn = "Full name of the corpsman: " + input("Full name of the corpsman: ")
            doctor_fn = "Full name of the doctor: " + input("Full name of the doctor: ")
            brg = Brigade(self.db_directory, br_num, c_num, driver_fn, corpsman_fn, doctor_fn)
            self.ambulance_brigades.update([(br_num, brg)])
            added_brigade = et.SubElement(self.tree_root, "brigade_{}".format(br_num.lstrip("Brigade number: ")))
            (lambda t: [et.SubElement(self.tree_root[len(self.tree_root)-1], "brigade_composition") for x in t])\
                (brg.brigade_composition())
            for i, each in enumerate(self.tree_root[len(self.tree_root)-1]):
                each.text = brg.brigade_composition()[i]
            else:
                self.tree.write(self.db_directory)
        else:
            print("Brigade number {} already exists.".format(br_num.lstrip("Brigade number: ")))

    def read_database(self):
        self.ambulance_number = self.tree_root[0].text
        for each in range(len(self.tree_root) - 1):
            brg_num = self.tree_root[each + 1][0].text
            coach_num = self.tree_root[each + 1][1].text
            driver_fn = self.tree_root[each + 1][2].text
            corpsman_fn = self.tree_root[each + 1][3].text
            doctor_fn = self.tree_root[each + 1][4].text
            brg = Brigade(self.db_directory, brg_num, coach_num, driver_fn, corpsman_fn, doctor_fn)
            for i in range(5, len(self.tree_root[each + 1])):
                brg.read_call(self.tree_root[each + 1][i][0].text)
                last_call = brg.brigade_calls[list(brg.brigade_calls.keys())[len(brg.brigade_calls) - 1]]
                last_call.call_number = self.tree_root[each + 1][i][0].text
                last_call.diagnosis = self.tree_root[each + 1][i][1].text
                last_call.address.street = self.tree_root[each + 1][i][2].text
                last_call.address.house_number = self.tree_root[each + 1][i][3].text
                last_call.address.flat_number = self.tree_root[each + 1][i][4].text
                last_call.address.caller_fn = self.tree_root[each + 1][i][5].text
                last_call.address.date = self.tree_root[each + 1][i][6].text
                last_call.address.time = self.tree_root[each + 1][i][7].text
                last_call.address.patient_fn = self.tree_root[each + 1][i][8].text
                last_call.address.patient_age = self.tree_root[each + 1][i][9].text
            self.ambulance_brigades.update([(brg_num, brg)])


class Brigade:
    def __init__(self, db_directory, brigade_number, c_num, driver_fn, corpsman_fn, doctor_fn):
        self.brigade_calls = {}
        self.functions_brigade = {"1. Create new call": self.new_call,
                                  "2. Delete call": self.delete_call,
                                  "3. Show call information": self.show_call_info,
                                  "4. Show brigade information": self.show_brigade_info,
                                  "0. Close brigade editor": self.close_brigade}
        self.db_directory = db_directory
        self.brigade_number = brigade_number
        self.coach_number = c_num
        self.driver_full_name = driver_fn
        self.corpsman_full_name = corpsman_fn
        self.doctor_full_name = doctor_fn
        self.tree = et.parse(self.db_directory)
        self.tree_root = self.tree.getroot()

    def close_brigade(self):
        self.checker = False
        ambl = Ambulance()
        ambl.read_database()
        ambl.start_ambulance_control()

    def start_brigade_control(self):
        def brigade_control():
            self.checker = True
            while self.checker:
                for each in list(self.functions_brigade.keys()):
                    print(each)
                inp = input("What to do: ")
                for i in list(self.functions_brigade.keys()):
                    if inp == i[:i.index(".")]:
                        self.tree = et.parse(self.db_directory)
                        self.tree_root = self.tree.getroot()
                        self.functions_brigade[i]()
                        break
                else:
                    print("Invalid input.")
        thr2 = threading.Thread(target=brigade_control)
        thr2.start()

    def new_call(self):
        call_num = "Call #" + input("Call number: ")
        if call_num not in list(self.brigade_calls.keys()):
            diagnosis = "Diagnosis of the patient: " + input("Diagnosis of the patient: ")
            cl = Call(self.db_directory, self.brigade_number, call_num, diagnosis)
            cl.new_address()
            cl.callsave()
            self.brigade_calls.update([(call_num, cl)])
        else:
            print("{} already exists.".format(call_num))

    def delete_call(self):
        if len(self.brigade_calls.keys()) != 0:
            print("Available calls: " + ", ".join([x.lstrip("Call #") for x in list(self.brigade_calls.keys())]))
            inp = input("Enter the number of call to delete: ")
            if inp != 0:
                if inp in [x.lstrip("Call #") for x in list(self.brigade_calls.keys())]:
                    self.tree_root.find("brigade_{}".format(self.brigade_number.lstrip("Brigade number: "))).remove(
                        self.tree_root.find("brigade_{}".format(self.brigade_number.lstrip("Brigade number: "))).find(
                            "call_{}".format(inp)))
                    self.brigade_calls.pop("Call #" + inp)
                else:
                    print("There is no such call.")
        else:
            print("There is still no call.")

    def show_call_info(self):
        if len(self.brigade_calls.keys()) != 0:
            print("Available calls: " + ", ".join([x.lstrip("Call #") for x in list(self.brigade_calls.keys())]))
            inp = input("Enter the number of call to show: ")
            if inp in [x.lstrip("Call #") for x in list(self.brigade_calls.keys())]:
                print("\n".join(self.brigade_calls["Call #{}".format(inp)].call_info()) + "\n")

            else:
                print("There is no such call.")
        else:
            print("There is still no call.")

    def read_call(self, call_num):
        cl = Call(self.db_directory, self.brigade_number)
        self.brigade_calls.update([(call_num, cl)])

    def show_brigade_info(self):
        print("\n".join(self.brigade_composition()) + "\n")

    def brigade_composition(self):
        brg_comp = []
        brg_comp.append(self.brigade_number)
        brg_comp.append(self.coach_number)
        brg_comp.append(self.driver_full_name)
        brg_comp.append(self.corpsman_full_name)
        brg_comp.append(self.doctor_full_name)
        return brg_comp


class Call:
    def __init__(self, db_directory, brigade_num, call_number="", diagnosis=""):
        self.diagnosis = diagnosis
        self.upper_brigade = brigade_num
        self.call_number = call_number
        self.db_directory = db_directory
        self.address = Address()
        self.tree = et.parse(self.db_directory)
        self.tree_root = self.tree.getroot()

    def callsave(self):
        cur_brg = self.tree_root.find("brigade_{}".format(self.upper_brigade.lstrip("Brigade number: ")))
        temporary = et.SubElement(cur_brg, "call_{}".format(self.call_number.lstrip("Call #")))
        for each in self.call_info():
            call_item = et.SubElement(temporary, "call_info")
            call_item.text = each
        self.tree.write(self.db_directory)

    def call_info(self):
        ci = list()
        ci.append(self.call_number)
        ci.append(self.diagnosis)
        ci.append(self.address.street)
        ci.append(self.address.house_number)
        ci.append(self.address.flat_number)
        ci.append(self.address.caller_fn)
        ci.append(self.address.date)
        ci.append(self.address.time)
        ci.append(self.address.patient_fn)
        ci.append(self.address.patient_age)
        return ci

    def new_address(self):
        street = "Street of the patient: " + input("Street of the patient: ")
        house_num = "House number: " + input("House number: ")
        flat_num = "Flat number: " + input("Flat number: ")
        caller_fn = "Full name of the caller: " + input("Full name of the caller: ")
        date = "Call date: " + input("Call date (DD.MM.YYYY): ")
        time = "Call time: " + input("Call time (HH:MM): ")
        patient_fn = "Full name of the patient: " + input("Full name of the patient: ")
        patient_age = "Patient age: " + input("Patient age: ")
        self.address = Address(street, house_num, flat_num, caller_fn, date, time, patient_fn, patient_age)


class Address:
    def __init__(self,street="",house_num="",flat_num="",caller_fn="",date="", time="", patient_fn="", patient_age=""):
        self.street = street
        self.house_number = house_num
        self.flat_number = flat_num
        self.caller_fn = caller_fn
        self.date = date
        self.time = time
        self.patient_fn = patient_fn
        self.patient_age = patient_age


if __name__ == "__main__":
    amb = Ambulance()
    amb.read_database()
    amb.start_ambulance_control()