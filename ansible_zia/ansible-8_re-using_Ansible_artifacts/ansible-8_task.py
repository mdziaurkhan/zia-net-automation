  vars:
    user_created_by_lookup: {'admin1':'admin123!', 'admin2':'admin123!' }     # dictionary

  - name: "Configuring 2 users using with_<lookup> and dictionary"
    ios_config:
      lines:
        - "username {{item.key}} privilege 15 secret {{item.value}}"
    with_dict: "{{ user_created_by_lookup }
