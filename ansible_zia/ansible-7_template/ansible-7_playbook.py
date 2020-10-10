- name: Router Template
  hosts: localhost
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
        private: yes
        confirm: yes

      - name: enable_password_creation
        prompt: "enable password"
        private: yes
        default: "zia123"
