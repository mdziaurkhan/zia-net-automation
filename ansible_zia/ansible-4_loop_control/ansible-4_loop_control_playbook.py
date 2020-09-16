- hosts: routers
  gather_facts: no

  vars:
    user_created_by_lookup: {'admin1':'admin123!', 'admin2':'admin123!', 'admin3':'admin123!' }     # dictionary
    user_created_by_loop: {'admin4':'admin123!', 'admin5':'admin123!', 'admin6':'admin123!' }       # dictionary

    loopback_created_by_lookup: [11,12,13]                 #list
    loopback_created_by_loop: [14,15,16]                   #list
  tasks:
  - name: "Configuring 3 users using with_<lookup> and dictionary"
    ios_config:
      lines:
        - "username {{item.key}} privilege 15 secret {{item.value}}"
    with_dict: "{{ user_created_by_lookup }}"

  - name: "configuring anohter 3 usrs using loop and dictionary"
    ios_config:
      lines:
        - "username {{item.key}} privilege 15 secret {{item.value}}"
    loop: "{{user_created_by_loop|dict2items}}"
    loop_control:          #To limit the displayed output, use the label directive with loop_control
      label: "{{ item.key }}"
      pause: 3      # it will pasue for 3 sec before it goes to next item.

  - name: "tracking of loop"
    debug:
      msg: "{{ item }} with index {{ my_idx }}"
    loop: "{{user_created_by_loop|dict2items}}"
    loop_control:
      index_var: my_idx  #To keep track of where you are in a loop, use the index_var directive with loop_control
