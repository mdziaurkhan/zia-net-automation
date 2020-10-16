re-using-ansible-artifacts
https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse.html#re-using-ansible-artifacts

You can write a simple playbook in one very large file, and most users learn the one-file approach first.
However, breaking tasks up into different files is an excellent way to organize complex sets of tasks and reuse them.
Smaller, more distributed artifacts let you re-use the same variables, tasks, and plays in multiple playbooks to address different use cases. .

Ansible offers four distributed, re-usable artifacts: variables files, task files, playbooks, and roles.
A variables file contains only variables.
A task file contains only tasks.
A playbook contains at least one play, and may contain variables, tasks, and other content.
  You can re-use tightly focused playbooks, but you can only re-use them statically, not dynamically.
A role contains a set of related tasks, variables, defaults, handlers, and even modules or other plugins in a defined file-tree.
  Unlike variables files, task files, or playbooks, roles can be easily uploaded and shared via Ansible Galaxy. See Roles for details about creating and using roles.



  Objectives:
re-using Ansible artifacts:
  i) import_playbook:
       we will  import  project-1 and 2 playbooks for this
      project playbook.

  ii) import_task:
  ii) include_vars:
      we will use our project 1 vars in this project

that means we are going to reuse our esisting paybook
and vars .

we have to write a palybooks where we will include
those playbooks and vars.
