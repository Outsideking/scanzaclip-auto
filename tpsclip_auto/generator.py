def generate_commands(dom_structure):
    commands = []
    for inp in dom_structure['inputs']:
        commands.append(f"fill_field('{inp}', '<value>')")
    for btn in dom_structure['buttons']:
        commands.append(f"click_button('{btn}')")
    return commands
