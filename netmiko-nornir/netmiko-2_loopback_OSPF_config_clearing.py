#! /usr/bin/env python3 
from netmiko import ConnectHandler
import time

switches = ['192.168.122.10', '192.168.122.20', '192.168.122.30', '192.168.122.40']
show_commands = ['show ip arp', 'show ip route', 'show ip interface brief | in up']
ospf_show_commands = ['show ip route ospf', 'show ip ospf neighbor']

# variable for loopback interface ip
l= 10
#variable for fa1/0 interface ip
f= 1
# variable for OSPF 
o= 10

for switch in switches:
    switch_connection = {'device_type': 'cisco_ios', 'host': switch, 'username': 'zia', 'password': 'zia123', 'ssh_config_file': '/etc/ssh/ssh_config'}
    net_connect = ConnectHandler(**switch_connection)
#show commands output before configuring the router 
    print("=================BEFORE==============",net_connect.find_prompt(),"===============BEFORE=============")
    a= 0
    for a in range(len(show_commands)):
        print(net_connect.find_prompt(),show_commands[a],)
        print(net_connect.send_command(show_commands[a]),'\n')
#configuring loopback intrface
    print("======Configuring lo0=======",net_connect.find_prompt(),"=====Configuring lo0=============")
    v_l_ip = '172.16.{}.1'
    l_ip =v_l_ip.format(l)
    #loopback interface details
    loopback_0 ={ 'lo0_name': 'loopback 0', 'lo0_ip': l_ip , 'lo0_netmask': '255.255.255.0'}
    # loopback interface config commands
    loopback_0_config = ['interface {}'.format(loopback_0['lo0_name']), 'ip address {} {}'.format(loopback_0['lo0_ip'],loopback_0['lo0_netmask']),'no shutdown']
    #seinding the command to Router
    print(net_connect.send_config_set(loopback_0_config),'\n')
    l += 10
#configuring fa1/0 intrface
    print("======Configuring fa1/0=======",net_connect.find_prompt(),"=====Configuring fa1/0=============")
    v_f_ip = '172.16.5.{}'
    f_ip =v_f_ip.format(f)
    #fa1/0 interface details
    fa1_0 ={ 'fa_name': 'fa1/0', 'fa_ip': f_ip , 'fa_netmask': '255.255.255.0'}
    # fa1/0 interface config commands
    fa1_0_config = ['interface {}'.format(fa1_0['fa_name']), 'ip address {} {}'.format(fa1_0['fa_ip'],fa1_0['fa_netmask']),'no shutdown']
    #seinding the command to Router
    print(net_connect.send_config_set(fa1_0_config),'\n')
    f += 1
#configuring ospf
    print("======Configuring OSPF=======",net_connect.find_prompt(),"=====Configuring OSPF=============")
    local_area = 'network 172.16.{}.0 0.0.0.255 area {}'
    local_area_command = local_area.format(o,o)
    ospf_config = ['router ospf 1', 'network 172.16.5.0 0.0.0.255 area 0', local_area_command]
    print(net_connect.send_config_set(ospf_config),'\n')
    o += 10
#show commands output after configuring the router 
    print("=================AFTER==============",net_connect.find_prompt(),"===============AFTER=============")
    a= 0
    for a in range(len(show_commands)):
        print(net_connect.find_prompt(),show_commands[a],)
        print(net_connect.send_command(show_commands[a]),'\n')
#wait for 30 sec to establish and propagate ospf and its topology
print ('*******Please wait 30 sec so that OSPF neighbourship and topology can be built*********')
time.sleep(30)

for switch in switches:
    switch_connection = {'device_type': 'cisco_ios', 'host': switch, 'username': 'zia', 'password': 'zia123', 'ssh_config_file': '/etc/ssh/ssh_config'}
    net_connect = ConnectHandler(**switch_connection)
#show commands output for OSPF after applying all the config
    print("====after applying all the config ospf==============",net_connect.find_prompt(),"============")
    b= 0
    for b in range(len(ospf_show_commands)):
        print(net_connect.find_prompt(),ospf_show_commands[b])
        print(net_connect.send_command(ospf_show_commands[b]),'\n')

