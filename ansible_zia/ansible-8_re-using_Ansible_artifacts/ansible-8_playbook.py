
  - name: "importing project-1 playbook"
    import_playbook: /home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-1_Connecting_devices/ansible-1_playbook.yaml

  - name: "importing project-2 playbook"
    import_playbook: /home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-2_loopback_ospf/ansible-2_loopback-ospf-playbook.yaml

  - hosts: routers
    gather_facts: no

    tasks:
       - name: "by using include_vars add connection variables"
         include_vars:
            file: /home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-1_Connecting_devices/group_vars/routers
       - name: " create 2 users by using include_tasks "
         include_tasks: ansible-8_task.py
         vars:
            user_created_by_lookup: {'admin1':'admin123!', 'admin2':'admin123!' }
