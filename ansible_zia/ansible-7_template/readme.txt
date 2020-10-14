Scripting: Python-Ansible#7 ( Template)
===========================
ansible template info:
https://docs.ansible.com/ansible/2.5/modules/template_module.html

All network engineers use some sort of templateing for their jobs. Sometimes we have to configure multiple switches/routers/firewalls where all the configurations are same except few parameters , right?
Template saves lots of our work and time.

1) ansible Templates are processed by the Jinja2 templating language
do not worry about jinja2, if you are not familiar with jinga2 , just find below information for jinja2
   {{  }}  = used  for variable
   {%  %} = used for command

2) in this lab i used vars_prompt , so that i can provide the information ( variables which are different for different routers ) when i run the playbook.
	in my playbook you will find below -
	i) - name: password_input
        prompt: "Password for username(user which you created in previous step)"
        private: yes              #it will not show the chracters what you are typing
        confirm: yes              # it will ask the password twice to make sure you type it right, if you type different then it will say password does not match and ask you to retype.

	ii)
     - name: enable_password_input
        prompt: "enable password"
        private: yes
        default: "zia123"     # if you do not type anything then it will automatically take the default value zia123

2)  my template file is " ansible-7_router_template.j2 " which we will use as the source file when we run the task in playbook ( template)
     and we will save our config file in  " routers_config_files" folder according to the router hostname
like below -
tasks:
     - name: "Create {{hostname_input}} configuration"
       template:
          src=/home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-7_template/ansible-7_router_template.j2
          dest=/home/mdziaurkhan/zia-net-automation/ansible_zia/ansible-7_template/routers_config_files/{{hostname_input}}.conf

3) lastly i have encrypted my host vars with ansible vault . as we are running this one our local machine so host will be local machine.

ansible_user: mdziaurkhan
ansible_ssh_pass: XXXXXXXXX
ansible_connection: local

you can find all the files realted to lab here : https://github.com/mdziaurkhan/zia-net-automation
#ansible #GNS3 #network_automation #scripting #Ubuntu
