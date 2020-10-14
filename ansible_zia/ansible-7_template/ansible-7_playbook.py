- name: Router Template
  hosts: local
  gather_facts: no

  #vars:
  #enable_password_creation_default = yes


  vars_prompt:

      - name: hostname_input
        prompt: "What is the name of the router"
        private: no

      - name: username_input
        prompt: "what is the admin username of the router"
        private: no

      - name: password_input
        prompt: "Password for username(user which you created in previous step)"
        private: yes              #it will not show the chracters what you are typing
        confirm: yes              # it will ask the password twice to make sure you type it right, if you type different then it will say password does not match and ask you to retype.

      - name: enable_password_input
        prompt: "enable password"
        private: yes
        default: "zia123"     # if you do not type anything then it will automatically take the default value zia123

  tasks:
     - name: "Create {{hostname_input}} configuration"
       template:
          src=/home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-7_template/ansible-7_router_template.j2
          dest=/home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-7_template/routers_config_files/{{hostname_input}}.conf
