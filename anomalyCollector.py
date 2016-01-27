#!/usr/bin/env python2

"""
Use pycomm python2 module to communicate with contrologix PLCs

adapted from: examples/test_ab_comm.py
more on: https://github.com/ruscito/pycomm
"""

# import logging
import MySQLdb as mdb
import time
import string
import datetime

from pycomm.ab_comm.clx import Driver as ClxDriver

PLC_IPS = {
    'plc1': '192.168.1.10',
    'tag_plc1':['HMI_FIT101.Pv', 'HMI_LIT101.Pv'],
    # 'tag_plc1':['HMI_FIT101.SAHH', 'HMI_FIT101.SAH', 'HMI_FIT101.SAL', 'HMI_FIT101.SALL',
    #             'HMI_LIT101.SAHH', 'HMI_LIT101.SAH', 'HMI_LIT101.SAL', 'HMI_LIT101.SALL',
    #             'HMI_FIT201.SAHH', 'HMI_FIT201.SAH', 'HMI_FIT201.SAL', 'HMI_FIT201.SALL'],
    'plc2': '192.168.1.20',
    # 'tag_plc2':['HMI_AIT201.SAHH', 'HMI_AIT201.SAH', 'HMI_AIT201.SAL', 'HMI_AIT201.SALL',
    #             'HMI_AIT202.SAHH', 'HMI_AIT202.SAH', 'HMI_AIT202.SAL', 'HMI_AIT202.SALL',
    #             'HMI_AIT203.SAHH', 'HMI_AIT203.SAH', 'HMI_AIT203.SAL', 'HMI_AIT203.SALL'], 
    'tag_plc2':['HMI_FIT201.Pv'],

    'plc3': '192.168.1.30',
    # 'tag_plc3':['HMI_LIT301.Pv', 'HMI_FIT301.Pv', 'HMI_FIT201.Pv','AI_FIT_301_FLOW'],
    'tag_plc3':['HMI_FIT201.Pv', 'HMI_FIT301.Pv', 'HMI_LIT201.Pv'],
    'plc4': '192.168.1.40',
    'tag_plc4':['HMI_LIT401.Pv','AI_FIT_401_FLOW'],
    'plc5': '192.168.1.50',
    'plc6': '192.168.1.60',
    'plc1r': '192.168.1.11',
    'plc2r': '192.168.1.21',
    'plc3r': '192.168.1.31',
    'plc4r': '192.168.1.41',
    'plc5r': '192.168.1.51',
    'plc6r': '192.168.1.61',
}


# init client
# logging.basicConfig(
#     filename="plc.log",
#     # level=logging.WARNING,
#     level=logging.DEBUG,  # more verbosity
#     format="%(levelname)-10s %(asctime)s %(message)s"
# )


def test_plc_write(plc_ip, tag_name, value, tag_type):
    """Write a plc tag and print a BOOL status code.

    :plc_ip: TODO
    :tag_name: TODO
    :value: TODO
    :tag_type: TODO

    """
    plc = ClxDriver()
    if plc.open(plc_ip):
        print(plc.write_tag(tag_name, value, tag_type))
        plc.close()
    else:
        print("Unable to open", plc_ip)


def test_plc_read(plc_ip, tag_name):
    """Read a plc tag and print the rx data

    :plc_ip:
    :tag_name:
    """

    plc = ClxDriver()
    if plc.open(plc_ip):

        print(plc.read_tag(tag_name))
    #plc.read_tag(tag_name)
        plc.close()
    else:
        print("Unable to open", plc_ip)

def test_plc_read_val(plc_ip, tag_name):
    """Read a plc tag and print the rx data

    :plc_ip:
    :tag_name:
    """

    plc = ClxDriver()
    if plc.open(plc_ip):
        tagg = plc.read_tag(tag_name)
        plc.close()
        return (tagg)
        
    else:
        print("Unable to open", plc_ip)


def main():
    """ Read and write PLCs tags using pycomm.

    DI_P_201* tags are configured as external tags with
    read/write permission. PLC2 will re-scan and re-write
    their value according to a set of state variables.

    dummy and dummy_int are configured as external tags
    with read/write permissions and they serve as a proof
    that pycomm can effectivley read and write tag using
    ENIP.
    """
    ## real SWAT tags
# connect to swatPLCdb
connect = mdb.connect('localhost', 'root', 'swat', 'swatPLCdb');
# var_name = ["\'HMI_LIT101.Pv\'","\'HMI_FIT101.Pv\'","\'HMI_P1_STATE\'", "\'HMI_P101.Status\'", "\'HMI_FIT201.Pv\'", "\'HMI_MV101.Status\'"]
# var_name_plc1 = ["\'HMI_FIT101.SAHH\'", "\'HMI_FIT101.SAH\'", "\'HMI_FIT101.SAL\'", "\'HMI_FIT101.SALL\'",
#                  "\'HMI_LIT101.SAHH\'", "\'HMI_LIT101.SAH\'", "\'HMI_LIT101.SAL\'", "\'HMI_LIT101.SALL\'",
#                  "\'HMI_FIT201.SAHH\'", "\'HMI_FIT201.SAH\'", "\'HMI_FIT201.SAL\'", "\'HMI_FIT201.SALL\'"]
var_name_plc1 = ["\'HMI_FIT101.Pv\'", "\'HMI_LIT101.Pv\'"]

var_name_plc2 = ["\'HMI_FIT201.Pv\'"]

# var_name_plc3 = ["\'HMI_FIT201.Pv\'", "\'HMI_FIT301.Pv\'", "\'HMI_LIT301.Pv\'"]

var_name_spc = ["\'HMI_FIT101.SAHH\'", "\'HMI_FIT101.SAH\'", "\'HMI_FIT101.SAL\'", "\'HMI_FIT101.SALL\'",
                "\'HMI_LIT101.SAHH\'", "\'HMI_LIT101.SAH\'", "\'HMI_LIT101.SAL\'", "\'HMI_LIT101.SALL\'",
                "\'HMI_FIT201.SAHH\'", "\'HMI_FIT201.SAH\'", "\'HMI_FIT201.SAL\'", "\'HMI_FIT201.SALL\'",
                "\'HMI_AIT201.SAHH\'", "\'HMI_AIT201.SAH\'", "\'HMI_AIT201.SAL\'", "\'HMI_AIT201.SALL\'",
                "\'HMI_AIT202.SAHH\'", "\'HMI_AIT202.SAH\'", "\'HMI_AIT202.SAL\'", "\'HMI_AIT202.SALL\'",
                "\'HMI_AIT203.SAHH\'", "\'HMI_AIT203.SAH\'", "\'HMI_AIT203.SAL\'", "\'HMI_AIT203.SALL\'"]

insert = """INSERT INTO anomalies(tag_name, tag_value)
            VALUES ({0}, {1});"""



print(datetime.datetime.now())

a = 0;
import anomaliesCheck
array1 = test_plc_read_val(PLC_IPS['plc1'], PLC_IPS['tag_plc1'])
array2 = test_plc_read_val(PLC_IPS['plc2'], PLC_IPS['tag_plc2'])
cur = connect.cursor()
    # for i in range(1, 11):
        # refresh data every 10 seconds
# cur.execute(insert.format(0, var_name_plc2[0], array1[0][1]))
# cur.execute(insert.format(0, var_name_plc2[1], array1[1][1]))
# cur.execute(insert.format(0, var_name_plc2[2], array1[2][1]))
# cur.execute(insert.format(0, var_name_plc2[3], array1[3][1]))
# cur.execute(insert.format(0, var_name_plc2[4], array1[4][1]))
# cur.execute(insert.format(0, var_name_plc2[5], array1[5][1]))
# cur.execute(insert.format(0, var_name_plc2[6], array1[6][1]))
# cur.execute(insert.format(0, var_name_plc2[7], array1[7][1]))
# cur.execute(insert.format(0, var_name_plc2[8], array1[8][1]))
# cur.execute(insert.format(0, var_name_plc2[9], array1[9][1]))
# cur.execute(insert.format(0, var_name_plc2[10], array1[10][1]))
# cur.execute(insert.format(0, var_name_plc2[11], array1[11][1]))
# connect.commit()

# import anomaliesCheck



for h in range(15):

    array1 = test_plc_read_val(PLC_IPS['plc1'], PLC_IPS['tag_plc1'])
    array2 = test_plc_read_val(PLC_IPS['plc2'], PLC_IPS['tag_plc2'])
    	# get 2 readings to compare
    	# for i in range(2):
    cur.execute(insert.format(var_name_plc1[0], array1[0][1]))
    cur.execute(insert.format(var_name_plc1[1], array1[1][1]))
    cur.execute(insert.format(var_name_plc2[0], array2[0][1]))
    anomaliesCheck.check()
    connect.commit()
    # cur.execute("DELETE FROM anomalies WHERE tag_name=\'HMI_FIT101.Pv\';") # delete the data set if there is no anomaly
    # cur.execute("DELETE FROM anomalies WHERE tag_name=\'HMI_FIT201.Pv\';") # delete the data set if there is no anomaly
    # cur.execute("DELETE FROM anomalies WHERE tag_name=\"HMI_LIT101.Pv\';") # delete the data set if there is no anomaly
    time.sleep(5) # wait for 5 seconds
connect.close() # close database connection
print(datetime.datetime.now())


if __name__ == '__main__':
    main()
