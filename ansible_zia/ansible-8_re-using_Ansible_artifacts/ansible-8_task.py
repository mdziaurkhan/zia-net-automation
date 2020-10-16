  - name: "Configuring 2 users using with_<lookup> and dictionary"
    ios_config:
      lines:
        - "username {{item.key}} privilege 15 secret {{item.value}}"
        #- "username test privilege 15 secret zia123"
    with_dict: "{{ user_created_by_lookup }}"
