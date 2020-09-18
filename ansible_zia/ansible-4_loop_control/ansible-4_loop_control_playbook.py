- hosts: routers
  gather_facts: no

  vars:
    user_created_by_lookup: {'admin1':'admin123!', 'admin2':'admin123!' }     # dictionary
    user_created_by_loop: {'admin4':'admin123!', 'admin5':'admin123!' }       # dictionary

  tasks:
  - name: "Configuring 2 users using with_<lookup> and dictionary"
    ios_config:
      lines:
        - "username {{item.key}} privilege 15 secret {{item.value}}"
    with_dict: "{{ user_created_by_lookup }}"

  - name: "configuring anohter 2 usrs using loop and dictionary"
    ios_config:
      lines:
        - "username {{item.key}} privilege 15 secret {{item.value}}"
    loop: "{{user_created_by_loop|dict2items}}"
    loop_control:
      label: "{{ item.key }}"  #To limit the displayed output, use the label directive with loop_control
      pause: 3      # it will pasue for 3 sec before it goes to next item.

  - name: "tracking of loop"
    debug:
      msg: "{{ item }} with index {{ my_idx }}"
    loop: "{{user_created_by_loop|dict2items}}"
    loop_control:
      index_var: my_idx  #To keep track of where you are in a loop, use the index_var directive with loop_control
