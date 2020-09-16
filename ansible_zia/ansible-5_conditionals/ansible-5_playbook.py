- hosts: routers
  gather_facts: no

  tasks:
  - name: "show hostname"
    ios_command:
      commands:
        - show run | i hostname

    register: output

  - name: "show output with when conditions"
    when: '"ziaR1" in "{{output.stdout}}"'
    debug:
      msg: "{{ output}}"
