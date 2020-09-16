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

  - name: "Configuring 3 loopback interfaces using with_<lookup> and list"
    ios_config:
      lines:
        - "interface loopback {{ item }}"
    with_items: "{{ loopback_created_by_lookup }}"

  - name: "configuring anohter 3 loopback interfaces using loop and list"
    ios_config:
      lines:
        - "interface loopback {{ item }}"
    loop: "{{ loopback_created_by_loop }}"
