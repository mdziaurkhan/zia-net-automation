
  - name: "importing project-1 playbook"
    import_playbook: /home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-1_Connecting_devices/ansible-1_playbook.yaml

  - name: "importing project-2 playbook"
    import_playbook: /home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-2_loopback_ospf/ansible-2_loopback-ospf-playbook.yaml

  #- import_tasks: ansible-8_task.py
    #hosts: routers
    #vars:
       #import_vars: /home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-1_Connecting_devices/group_vars/routers
