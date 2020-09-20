Objectives:
Ansible vault:
  i) using anisble vault we will encrypt our group_vars
data so that no one can see our username and password.

ansible-vault encrypt      [will use password zia]

  ii) change/rekey the vault password.

ansible-vault rekey      [ will use password zia123]

 iii) edit and view encrypted file

ansible-vault edit

 iv) only view the encrypted file without edit.

ansible-vault view

 v)  run the playbook

-- ask-vault-pass


Note: for this lab i am re-using my project-5
( ansible-5_conditionals) lab
